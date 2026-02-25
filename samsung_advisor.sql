--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: samsung_phones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.samsung_phones (
    id integer NOT NULL,
    model_name character varying(255),
    release_date character varying(50),
    display text,
    battery text,
    camera text,
    ram character varying(100),
    storage character varying(100),
    price character varying(100)
);


ALTER TABLE public.samsung_phones OWNER TO postgres;

--
-- Name: samsung_phones_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.samsung_phones_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.samsung_phones_id_seq OWNER TO postgres;

--
-- Name: samsung_phones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.samsung_phones_id_seq OWNED BY public.samsung_phones.id;


--
-- Name: samsung_phones id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.samsung_phones ALTER COLUMN id SET DEFAULT nextval('public.samsung_phones_id_seq'::regclass);


--
-- Data for Name: samsung_phones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.samsung_phones (id, model_name, release_date, display, battery, camera, ram, storage, price) FROM stdin;
1	Samsung Galaxy S24 Ultra	2024, January 17	6.8 inches, 113.5 cm2 (~88.5% screen-to-body ratio)	Li-Ion 5000 mAh	\N	\N	256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM	$ 464.35 / € 664.75 / £ 524.85 / ₹ 89,999
2	Samsung Galaxy S24+	2024, January 17	6.7 inches, 110.2 cm2 (~91.6% screen-to-body ratio)	Li-Ion 4900 mAh	\N	\N	256GB 12GB RAM, 512GB 12GB RAM	$ 384.95 / € 460.67 / £ 428.00
3	Samsung Galaxy S24	2024, January 17	6.2 inches, 94.4 cm2 (~90.9% screen-to-body ratio)	Li-Ion 4000 mAh	\N	\N	128GB 8GB RAM, 256GB 8GB RAM, 256GB 12GB RAM, 512GB 8GB RAM	$ 298.44 / € 432.60 / £ 318.75 / ₹ 42,165
4	Samsung Galaxy S23 Ultra	2023, February 01	6.8 inches, 114.7 cm2 (~89.9% screen-to-body ratio)	Li-Ion 5000 mAh	\N	\N	256GB 8GB RAM, 256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM	$ 419.99 / € 419.99 / £ 399.00 / ₹ 79,999
5	Samsung Galaxy S23	2023, February 01	6.1 inches, 90.1 cm2 (~86.8% screen-to-body ratio)	Li-Ion 3900 mAh	\N	\N	128GB 8GB RAM, 256GB 8GB RAM, 512GB 8GB RAM	$ 242.44 / € 348.00 / £ 216.00 / ₹ 52,350
6	Samsung Galaxy S22 Ultra 5G	2022, February 09	6.8 inches, 114.7 cm2 (~90.2% screen-to-body ratio)	Li-Ion 5000 mAh	\N	\N	128GB 8GB RAM, 256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM	$ 279.99 / € 359.00 / £ 256.00
7	Samsung Galaxy A55	2024, March 11	6.6 inches, 106.9 cm2 (~85.8% screen-to-body ratio)	Li-Ion 5000 mAh	\N	\N	128GB 6GB RAM, 128GB 8GB RAM, 256GB 6GB RAM, 256GB 8GB RAM, 256GB 12GB RAM	$ 399.99 / € 279.46 / £ 214.74 / ₹ 25,999
8	Lava Yuva 2 Pro	2023, February 22	6.52 inches, 102.6 cm2 (~82.1% screen-to-body ratio)	Li-Po 5000 mAh	\N	\N	64GB 4GB RAM	About 90 EUR
9	TCL 505	2024, February 06	6.75 inches, 110.0 cm2 (~85.2% screen-to-body ratio)	5010 mAh	\N	\N	64GB 4GB RAM, 128GB 4GB RAM	\N
10	Samsung Galaxy A34	2023, March 14	6.6 inches, 106.9 cm2 (~84.9% screen-to-body ratio)	Li-Ion 5000 mAh	\N	\N	128GB 4GB RAM, 128GB 6GB RAM, 128GB 8GB RAM, 256GB 6GB RAM, 256GB 8GB RAM	€ 136.82 / £ 137.99 / ₹ 20,750
11	Honor X8b	2023, December 14	6.7 inches, 108.0 cm2 (~89.9% screen-to-body ratio)	Li-Po 4500 mAh	\N	\N	128GB 8GB RAM, 256GB 6GB RAM, 256GB 8GB RAM, 512GB 8GB RAM	$ 359.00 / € 134.26
12	Samsung Galaxy A05s	2023, September 25	6.7 inches, 108.4 cm2 (~82.9% screen-to-body ratio)	Li-Po 5000 mAh	\N	\N	64GB 4GB RAM, 128GB 4GB RAM, 128GB 6GB RAM	€ 109.99 / £ 91.20 / ₹ 17,499
13	Samsung Galaxy Z Fold5	2023, July 26	7.6 inches, 183.2 cm2 (~91.1% screen-to-body ratio)	Li-Po 4400 mAh	\N	\N	256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM	$ 524.97 / € 689.99 / £ 512.00 / ₹ 108,990
14	Samsung Galaxy Z Flip5	2023, July 26	6.7 inches, 102.0 cm2 (~85.9% screen-to-body ratio)	Li-Po 3700 mAh	\N	\N	256GB 8GB RAM, 512GB 8GB RAM	$ 333.17 / € 390.00 / £ 290.00 / ₹ 56,999
15	Samsung Galaxy Z Fold4	2022, August 10	7.6 inches, 183.2 cm2 (~90.9% screen-to-body ratio)	Li-Po 4400 mAh	\N	\N	256GB 12GB RAM, 512GB 12GB RAM, 1TB 12GB RAM	$ 378.99 / € 536.74 / £ 480.00 / ₹ 79,999
16	vivo Y33e	2022, May 30	6.51 inches, 102.3 cm2 (~82.2% screen-to-body ratio)	5000 mAh	\N	\N	128GB 4GB RAM	About 180 EUR
17	Samsung Galaxy S23 FE	2023, October 04	6.4 inches, 100.5 cm2 (~83.2% screen-to-body ratio)	Li-Ion 4500 mAh	\N	\N	128GB 8GB RAM, 256GB 8GB RAM	$ 189.54 / € 283.32 / £ 199.00
18	Samsung Galaxy S21 FE 5G	2022, January 04	6.4 inches, 100.5 cm2 (~86.7% screen-to-body ratio)	Li-Ion 4500 mAh	\N	\N	128GB 6GB RAM, 128GB 8GB RAM, 256GB 6GB RAM, 256GB 8GB RAM	$ 149.00 / € 185.00 / £ 149.00
19	OnePlus Nord N30	2023, June 06	6.72 inches, 109.6 cm2 (~87.1% screen-to-body ratio)	Li-Po 5000 mAh	\N	\N	128GB 8GB RAM	$ 129.99 / ₹ 1,599
20	Cubot P80	2023	6.58 inches, 104.3 cm2 (~83.0% screen-to-body ratio)	5200 mAh	\N	\N	256GB 8GB RAM, 512GB 8GB RAM	About 160 EUR
21	Oppo Reno8 T	2023, February 02	6.43 inches, 99.8 cm2 (~84.1% screen-to-body ratio)	Li-Po 5000 mAh	\N	\N	128GB 8GB RAM, 256GB 8GB RAM	About 490 EUR
22	Honor Magic V2	2023, July 12	7.92 inches, 201.6 cm2 (~88.5% screen-to-body ratio)	Si/C Li-Ion 5000 mAh	\N	\N	256GB 16GB RAM, 512GB 16GB RAM, 1TB 16GB RAM	$ 845.00 / € 704.01 / £ 714.38
23	Cubot Note 50	2023, July	6.56 inches, 103.4 cm2 (~82.3% screen-to-body ratio)	5200 mAh	\N	\N	256GB 8GB RAM	About 130 EUR
24	Samsung Galaxy XCover6 Pro	2022, June 29	6.6 inches, 104.9 cm2 (~77.8% screen-to-body ratio)	Li-Po 4050 mAh, removable	\N	\N	128GB 6GB RAM	$ 150.00 / € 159.89 / £ 189.00
\.


--
-- Name: samsung_phones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.samsung_phones_id_seq', 24, true);


--
-- Name: samsung_phones samsung_phones_model_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.samsung_phones
    ADD CONSTRAINT samsung_phones_model_name_key UNIQUE (model_name);


--
-- Name: samsung_phones samsung_phones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.samsung_phones
    ADD CONSTRAINT samsung_phones_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

