import pandas as pd
import psycopg2

# Read dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Connect PostgreSQL
conn = psycopg2.connect(
    database="sales_dw",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# ---------------------------
# CUSTOMER DIMENSION
# ---------------------------
customers = df[["Customer ID", "Customer Name", "Segment"]].drop_duplicates()

for _, row in customers.iterrows():
    cursor.execute("""
        INSERT INTO dim_customer
        (customer_id, customer_name, segment)
        VALUES (%s,%s,%s)
    """,
    (
        row["Customer ID"],
        row["Customer Name"],
        row["Segment"]
    ))

# ---------------------------
# PRODUCT DIMENSION
# ---------------------------
products = df[
    ["Product ID", "Product Name", "Category", "Sub-Category"]
].drop_duplicates()

for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO dim_product
        (product_id, product_name, category, sub_category)
        VALUES (%s,%s,%s,%s)
    """,
    (
        row["Product ID"],
        row["Product Name"],
        row["Category"],
        row["Sub-Category"]
    ))

# ---------------------------
# LOCATION DIMENSION
# ---------------------------
locations = df[
    ["Country", "State", "City", "Region", "Postal Code"]
].drop_duplicates()

for _, row in locations.iterrows():
    cursor.execute("""
        INSERT INTO dim_location
        (country,state,city,region,postal_code)
        VALUES (%s,%s,%s,%s,%s)
    """,
    (
        row["Country"],
        row["State"],
        row["City"],
        row["Region"],
        str(row["Postal Code"])
    ))

# ---------------------------
# DATE DIMENSION
# ---------------------------
dates = pd.to_datetime(df["Order Date"]).drop_duplicates()

for date in dates:
    cursor.execute("""
        INSERT INTO dim_date
        (order_date, year, month, day)
        VALUES (%s,%s,%s,%s)
    """,
    (
        date.date(),
        date.year,
        date.month,
        date.day
    ))

conn.commit()

cursor.close()
conn.close()

print("Dimension tables loaded successfully!")