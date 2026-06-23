CREATE DATABASE sales_dw;
CREATE TABLE dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    segment VARCHAR(50)
);

CREATE TABLE dim_location (
    location_key SERIAL PRIMARY KEY,
    country VARCHAR(50),
    state VARCHAR(50),
    city VARCHAR(50),
    region VARCHAR(50),
    postal_code VARCHAR(20)
);

CREATE TABLE dim_date (
    date_key SERIAL PRIMARY KEY,
    order_date DATE,
    year INT,
    month INT,
    day INT
);

CREATE TABLE fact_sales (
    sales_key SERIAL PRIMARY KEY,
    order_id VARCHAR(20),

    customer_key INT,
    product_key INT,
    location_key INT,
    date_key INT,

    sales NUMERIC,
    quantity INT,
    discount NUMERIC,
    profit NUMERIC
);

CREATE TABLE dim_product (
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(30),
    product_name VARCHAR(255),
    category VARCHAR(50),
    sub_category VARCHAR(50)
);

SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';

SELECT COUNT(*) FROM dim_customer;
SELECT COUNT(*) FROM dim_product;
SELECT COUNT(*) FROM dim_location;
SELECT COUNT(*) FROM dim_date;
