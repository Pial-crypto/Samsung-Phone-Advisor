# Samsung Phone Advisor

## How to Run the Project

Follow the steps below to set up and run the Samsung Phone Advisor system.

---

## 1. Clone the Repository

```bash
git clone https://github.com/Pial-crypto/Samsung-Phone-Advisor
cd samsung_phone_advisor
```

---

## 2. Create and Activate Virtual Environment

Create virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install fastapi uvicorn psycopg2-binary requests beautifulsoup4 python-dotenv
```

---

## 4. Setup PostgreSQL

Make sure:

- PostgreSQL is installed
- PostgreSQL service is running
- `psql` is available in your system

Update your database credentials inside:

```
database/db.py
```

Example configuration:

```python
DB_NAME = "samsung_advisor"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
```

---

## 5. Automatic Database Restore

This project includes a database dump file:

```
samsung_advisor.sql
```

If the database does not exist, the system will:

- Create the database automatically
- Restore tables and data from the `.sql` file
- Then execute the query

Make sure `psql` is properly configured in your system.

---

## 6. (Optional) Scrape Fresh Data

If you want to scrape updated Samsung phone data:

```bash
python main.py
```

If you see “Too Many Requests”, wait a few minutes and try again.

---

## 7. Run the API Server

Start the FastAPI server:

```bash
uvicorn api.main:app --reload
```

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

Use the `/ask` endpoint to test the system.

---

## Example Request

```json
{
  "question": "Compare Galaxy S23 Ultra and S22 Ultra"
}
```

The system will return specifications, comparisons, or recommendations depending on the query.