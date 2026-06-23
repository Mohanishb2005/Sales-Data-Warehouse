import pandas as pd
import psycopg2

df = pd.read_csv(
    r"C:\sales data warehouse\data\Sample - Superstore.csv",
    encoding="latin1"
)

conn = psycopg2.connect(
    database="sales_dw",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

for _, row in df.iterrows():

    # Customer Key
    cursor.execute("""
        SELECT customer_key
        FROM dim_customer
        WHERE customer_id = %s
    """, (row["Customer ID"],))

    customer_key = cursor.fetchone()[0]

    # Product Key
    cursor.execute("""
        SELECT product_key
        FROM dim_product
        WHERE product_id = %s
    """, (row["Product ID"],))

    product_key = cursor.fetchone()[0]

    # Location Key
    cursor.execute("""
        SELECT location_key
        FROM dim_location
        WHERE city=%s
        AND state=%s
    """, (
        row["City"],
        row["State"]
    ))

    location_key = cursor.fetchone()[0]

    # Date Key
    order_date = pd.to_datetime(row["Order Date"]).date()

    cursor.execute("""
        SELECT date_key
        FROM dim_date
        WHERE order_date=%s
    """, (order_date,))

    date_key = cursor.fetchone()[0]

    # Insert Fact
    cursor.execute("""
        INSERT INTO fact_sales
        (
            order_id,
            customer_key,
            product_key,
            location_key,
            date_key,
            sales,
            quantity,
            discount,
            profit
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        row["Order ID"],
        customer_key,
        product_key,
        location_key,
        date_key,
        row["Sales"],
        row["Quantity"],
        row["Discount"],
        row["Profit"]
    ))

conn.commit()

cursor.close()
conn.close()

print("Fact table loaded successfully!")