import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read from .env
DB_NAME = os.getenv("DB_NAME", "samsung_advisor")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

SQL_DUMP_FILE = "samsung_advisor.sql"


# -------------------------------------------------
# Database Connection
# -------------------------------------------------
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )


# -------------------------------------------------
# Insert Phone
# -------------------------------------------------
def insert_phone(data):
    if data is None:
        print("No data to insert for this phone.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO samsung_phones
    (model_name, release_date, display, battery, camera, ram, storage, price)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (model_name) DO NOTHING;
    """

    cursor.execute(query, (
        data.get("model_name"),
        data.get("release_date"),
        data.get("display"),
        data.get("battery"),
        data.get("camera"),
        data.get("ram"),
        data.get("storage"),
        data.get("price"),
    ))

    conn.commit()
    cursor.close()
    conn.close()



def get_all_model_names():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT model_name FROM samsung_phones;")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return [row[0] for row in results]



def restore_database():
    print("Restoring database from SQL dump file...")

    try:
        # Connect to default postgres DB
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}'"
        )
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Database '{DB_NAME}' created.")

        cursor.close()
        conn.close()

        # Restore from dump file
        os.system(
            f'psql -U {DB_USER} -d {DB_NAME} -f {SQL_DUMP_FILE}'
        )

        print("Database restored successfully.")

    except Exception as e:
        print("Failed to restore database:", e)


def get_phone_by_name(name):
    query = """
    SELECT model_name, release_date, display, battery, camera, ram, storage, price
    FROM samsung_phones
    WHERE model_name ILIKE %s
    """

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(query, ('%' + name + '%',))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result

    except OperationalError:
        print("Database connection failed. Attempting restore...")
        restore_database()

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(query, ('%' + name + '%',))
            result = cursor.fetchone()

            cursor.close()
            conn.close()

            return result

        except Exception:
            return None


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Database connected successfully")
        conn.close()
    except Exception as e:
        print("Connection failed")
        print(e)