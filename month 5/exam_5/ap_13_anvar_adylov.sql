--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: ap_13_anvar_adylov; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE ap_13_anvar_adylov WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1251';


ALTER DATABASE ap_13_anvar_adylov OWNER TO postgres;

\connect ap_13_anvar_adylov

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- Name: brands; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.brands (
    id integer NOT NULL,
    brand character varying(45) NOT NULL
);


ALTER TABLE public.brands OWNER TO postgres;

--
-- Name: brands_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.brands_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.brands_id_seq OWNER TO postgres;

--
-- Name: brands_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.brands_id_seq OWNED BY public.brands.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    category character varying(45) DEFAULT 'name category'::character varying NOT NULL,
    description character varying(100) DEFAULT NULL::character varying
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categories_id_seq OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: contragents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contragents (
    id integer NOT NULL,
    agent character varying(45) NOT NULL,
    address character varying(50),
    contacts character varying(50)
);


ALTER TABLE public.contragents OWNER TO postgres;

--
-- Name: contragents_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contragents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contragents_id_seq OWNER TO postgres;

--
-- Name: contragents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contragents_id_seq OWNED BY public.contragents.id;


--
-- Name: deliveries; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deliveries (
    id integer NOT NULL,
    action_date date NOT NULL,
    product_id integer NOT NULL,
    contragent_id integer NOT NULL,
    warehouse_id integer NOT NULL,
    quantity numeric(10,3) DEFAULT 0.000 NOT NULL
);


ALTER TABLE public.deliveries OWNER TO postgres;

--
-- Name: deliveries_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deliveries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deliveries_id_seq OWNER TO postgres;

--
-- Name: deliveries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deliveries_id_seq OWNED BY public.deliveries.id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer NOT NULL,
    category_id integer NOT NULL,
    brand_id integer,
    product character varying(45) NOT NULL,
    price numeric(10,2) DEFAULT 0.00,
    description character varying(100) DEFAULT NULL::character varying
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.products_id_seq OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: purchases; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.purchases (
    id integer NOT NULL,
    action_date date NOT NULL,
    product_id integer NOT NULL,
    warehouse_id integer NOT NULL,
    contragent_id integer NOT NULL,
    quantity numeric(10,3) DEFAULT 0.000 NOT NULL
);


ALTER TABLE public.purchases OWNER TO postgres;

--
-- Name: purchases_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.purchases_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.purchases_id_seq OWNER TO postgres;

--
-- Name: purchases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.purchases_id_seq OWNED BY public.purchases.id;


--
-- Name: transfers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transfers (
    id integer NOT NULL,
    action_date date NOT NULL,
    product_id integer NOT NULL,
    warehouse_sender_id integer NOT NULL,
    warehouse_recipient_id integer NOT NULL,
    quantity numeric(10,3) DEFAULT 0.000 NOT NULL
);


ALTER TABLE public.transfers OWNER TO postgres;

--
-- Name: transfers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.transfers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.transfers_id_seq OWNER TO postgres;

--
-- Name: transfers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.transfers_id_seq OWNED BY public.transfers.id;


--
-- Name: warehouses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.warehouses (
    id integer NOT NULL,
    warehouse character varying(45) NOT NULL
);


ALTER TABLE public.warehouses OWNER TO postgres;

--
-- Name: warehouses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.warehouses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.warehouses_id_seq OWNER TO postgres;

--
-- Name: warehouses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.warehouses_id_seq OWNED BY public.warehouses.id;


--
-- Name: brands id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.brands ALTER COLUMN id SET DEFAULT nextval('public.brands_id_seq'::regclass);


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: contragents id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contragents ALTER COLUMN id SET DEFAULT nextval('public.contragents_id_seq'::regclass);


--
-- Name: deliveries id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deliveries ALTER COLUMN id SET DEFAULT nextval('public.deliveries_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: purchases id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchases ALTER COLUMN id SET DEFAULT nextval('public.purchases_id_seq'::regclass);


--
-- Name: transfers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transfers ALTER COLUMN id SET DEFAULT nextval('public.transfers_id_seq'::regclass);


--
-- Name: warehouses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.warehouses ALTER COLUMN id SET DEFAULT nextval('public.warehouses_id_seq'::regclass);


--
-- Data for Name: brands; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.brands (id, brand) VALUES (1, 'Acer');
INSERT INTO public.brands (id, brand) VALUES (2, 'Dell');
INSERT INTO public.brands (id, brand) VALUES (3, 'Toshiba');
INSERT INTO public.brands (id, brand) VALUES (4, 'Nestle');
INSERT INTO public.brands (id, brand) VALUES (5, 'Shlurpo');
INSERT INTO public.brands (id, brand) VALUES (6, 'Nutella');
INSERT INTO public.brands (id, brand) VALUES (7, 'Samsung');
INSERT INTO public.brands (id, brand) VALUES (8, 'Apple');
INSERT INTO public.brands (id, brand) VALUES (9, 'John Brand');


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.categories (id, category, description) VALUES (1, 'Food item', 'Еда');
INSERT INTO public.categories (id, category, description) VALUES (2, 'Laptop', 'Ноутбук');
INSERT INTO public.categories (id, category, description) VALUES (3, 'Mobile Phone', 'Телефон, смартфон');
INSERT INTO public.categories (id, category, description) VALUES (4, 'Gizmo', 'гизмо');
INSERT INTO public.categories (id, category, description) VALUES (5, 'Monitor', 'Монитор');
INSERT INTO public.categories (id, category, description) VALUES (6, 'Keyboard', 'Клавиатура');
INSERT INTO public.categories (id, category, description) VALUES (7, 'Mouse', 'Компьютерная мышь');


--
-- Data for Name: contragents; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.contragents (id, agent, address, contacts) VALUES (1, 'John John', 'Elm Street 1428', NULL);
INSERT INTO public.contragents (id, agent, address, contacts) VALUES (2, 'Unka Plutt', 'Tatooine', NULL);
INSERT INTO public.contragents (id, agent, address, contacts) VALUES (3, 'Rob Schneider', 'Hollywood', NULL);
INSERT INTO public.contragents (id, agent, address, contacts) VALUES (4, 'Kid Napper', 'Abandoned factory, outskirts ', NULL);
INSERT INTO public.contragents (id, agent, address, contacts) VALUES (5, 'Global Trade Federation', 'Space station sector Earth', NULL);


--
-- Data for Name: deliveries; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (1, '2022-05-04', 2, 1, 1, 200.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (2, '2022-05-05', 4, 1, 1, 50.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (3, '2022-05-18', 7, 1, 1, 35.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (4, '2022-06-10', 3, 2, 2, 20.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (5, '2022-08-03', 10, 3, 1, 81.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (6, '2022-08-04', 4, 4, 3, 25.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (7, '2022-08-08', 5, 2, 4, 356.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (8, '2022-08-09', 6, 1, 4, 230.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (9, '2022-09-02', 3, 3, 2, 50.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (10, '2022-10-01', 1, 3, 5, 10000.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (11, '2022-10-01', 2, 1, 1, 350.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (12, '2022-10-03', 2, 1, 2, 400.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (13, '2022-12-02', 3, 5, 2, 41.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (14, '2022-12-08', 3, 3, 2, 11.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (15, '2022-12-09', 1, 2, 6, 340.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (16, '2023-01-04', 2, 1, 1, 159.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (17, '2023-01-04', 4, 5, 1, 230.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (18, '2023-01-05', 3, 4, 3, 17.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (19, '2023-02-02', 10, 1, 2, 26.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (20, '2023-03-12', 3, 4, 1, 31.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (21, '2023-05-06', 2, 1, 4, 20.000);
INSERT INTO public.deliveries (id, action_date, product_id, contragent_id, warehouse_id, quantity) VALUES (22, '2023-06-15', 3, 1, 2, 25.000);


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (2, 2, 1, 'Aspire Go Intel', 200000.00, 'Laptop 2 TB HDD');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (3, 4, 5, 'Iconic Jabba shlurpo', 9999999.00, 'Iconic shlurpo that belongs to Jabba');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (4, 5, 2, 'Monitor G6', 150000.00, '16:9 LSD screen');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (5, 1, 6, 'Chocolate spread', 564.00, 'chocolate in a jar');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (6, 1, 4, 'Chocolate bar', 800.00, 'a bar of chocolate');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (7, 2, 3, 'Laptop B88', 350000.00, '1 TB gaming laptop');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (8, 2, 2, 'Laptop C66', 285000.00, '720 GB SDD laptop');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (9, 3, 7, 'Samsung Galaxy S99', 900000.00, 'Smartphone');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (10, 3, 8, 'Iphone 54Pro', 950000.00, 'Smartphone but Apple ');
INSERT INTO public.products (id, category_id, brand_id, product, price, description) VALUES (1, 1, 4, 'Crispy breakfast', 250.00, 'breakfast food item');


--
-- Data for Name: purchases; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (1, '2023-06-06', 6, 4, 3, 300.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (4, '2023-06-08', 3, 2, 4, 15.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (5, '2023-07-01', 2, 3, 1, 5.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (6, '2023-07-17', 4, 1, 1, 30.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (7, '2023-08-03', 7, 1, 1, 9.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (8, '2023-08-03', 8, 1, 1, 4.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (9, '2023-09-02', 2, 2, 5, 13.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (10, '2023-09-06', 5, 4, 5, 19.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (11, '2023-09-08', 7, 6, 1, 15.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (12, '2024-01-01', 1, 5, 2, 21.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (13, '2024-01-05', 2, 3, 1, 10.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (14, '2024-02-03', 3, 2, 5, 36.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (15, '2024-02-05', 7, 5, 3, 26.000);
INSERT INTO public.purchases (id, action_date, product_id, warehouse_id, contragent_id, quantity) VALUES (16, '2023-11-10', 2, 3, 1, 20.000);


--
-- Data for Name: transfers; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (4, '2024-10-11', 2, 1, 2, 80.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (5, '2024-10-12', 4, 3, 4, 51.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (1, '2023-09-05', 5, 2, 4, 500.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (3, '2023-10-14', 9, 4, 1, 37.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (2, '2023-10-12', 3, 3, 2, 19.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (6, '2022-12-09', 6, 5, 6, 71.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (7, '2023-11-11', 3, 1, 2, 11.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (8, '2023-12-04', 5, 2, 4, 100.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (9, '2022-09-07', 4, 5, 1, 18.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (10, '2023-02-10', 1, 2, 3, 250.000);
INSERT INTO public.transfers (id, action_date, product_id, warehouse_sender_id, warehouse_recipient_id, quantity) VALUES (11, '2023-05-18', 7, 1, 4, 20.000);


--
-- Data for Name: warehouses; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.warehouses (id, warehouse) VALUES (1, 'John Warehouse');
INSERT INTO public.warehouses (id, warehouse) VALUES (2, 'Glopshitto');
INSERT INTO public.warehouses (id, warehouse) VALUES (3, 'Warepalace');
INSERT INTO public.warehouses (id, warehouse) VALUES (4, 'Big Ned');
INSERT INTO public.warehouses (id, warehouse) VALUES (5, 'Forgetfull Joe');
INSERT INTO public.warehouses (id, warehouse) VALUES (6, 'Three fingered Hose');


--
-- Name: brands_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.brands_id_seq', 9, true);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 7, true);


--
-- Name: contragents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contragents_id_seq', 5, true);


--
-- Name: deliveries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deliveries_id_seq', 22, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 10, true);


--
-- Name: purchases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.purchases_id_seq', 16, true);


--
-- Name: transfers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transfers_id_seq', 11, true);


--
-- Name: warehouses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.warehouses_id_seq', 6, true);


--
-- Name: brands brands_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.brands
    ADD CONSTRAINT brands_pkey PRIMARY KEY (id);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: categories category_unique; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT category_unique UNIQUE (category);


--
-- Name: contragents contragents_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contragents
    ADD CONSTRAINT contragents_pkey PRIMARY KEY (id);


--
-- Name: deliveries deliveries_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deliveries
    ADD CONSTRAINT deliveries_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: purchases purchases_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchases
    ADD CONSTRAINT purchases_pkey PRIMARY KEY (id);


--
-- Name: transfers transfers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transfers
    ADD CONSTRAINT transfers_pkey PRIMARY KEY (id);


--
-- Name: warehouses warehouses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.warehouses
    ADD CONSTRAINT warehouses_pkey PRIMARY KEY (id);


--
-- Name: deliveries fk_agent; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deliveries
    ADD CONSTRAINT fk_agent FOREIGN KEY (contragent_id) REFERENCES public.contragents(id);


--
-- Name: purchases fk_agent; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchases
    ADD CONSTRAINT fk_agent FOREIGN KEY (contragent_id) REFERENCES public.contragents(id);


--
-- Name: products fk_brand; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT fk_brand FOREIGN KEY (category_id) REFERENCES public.categories(id) ON UPDATE CASCADE;


--
-- Name: products fk_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT fk_category FOREIGN KEY (brand_id) REFERENCES public.brands(id) ON UPDATE CASCADE;


--
-- Name: deliveries fk_product; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deliveries
    ADD CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: purchases fk_product; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchases
    ADD CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: transfers fk_product; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transfers
    ADD CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: deliveries fk_warehouse; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deliveries
    ADD CONSTRAINT fk_warehouse FOREIGN KEY (warehouse_id) REFERENCES public.warehouses(id);


--
-- Name: purchases fk_warehouse; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchases
    ADD CONSTRAINT fk_warehouse FOREIGN KEY (warehouse_id) REFERENCES public.warehouses(id);


--
-- Name: transfers fk_warehouse_receiver; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transfers
    ADD CONSTRAINT fk_warehouse_receiver FOREIGN KEY (warehouse_recipient_id) REFERENCES public.warehouses(id);


--
-- Name: transfers fk_warehouse_sender; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transfers
    ADD CONSTRAINT fk_warehouse_sender FOREIGN KEY (warehouse_sender_id) REFERENCES public.warehouses(id);


--
-- PostgreSQL database dump complete
--

