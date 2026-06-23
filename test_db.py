import psycopg2

conn = psycopg2.connect(
    database="sales_dw",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
""")

print(cursor.fetchall())

cursor.close()
conn.close()