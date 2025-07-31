import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv("simulated_smart_log_dataset_with_serial.csv")

# Check data types
print(df.dtypes)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="workwatch_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert row-by-row
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO smart_logs (
            power_on_hours, temperature, reallocated_sectors_count,
            reported_uncorrectable_errors, spin_retry_count, seek_error_rate,
            udma_crc_error_count, prediction, serial_number, timestamp
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()