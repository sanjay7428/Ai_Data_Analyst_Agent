import pandas as pd
import sqlite3

# 1. Ask user for CSV file path
csv_path = input("Enter CSV file path: ")

# 2. Load CSV
df = pd.read_csv(csv_path)

print("\nColumns in dataset:")
print(df.columns.tolist())
DB_path = "E:\complate assignment for sql\ai_data_analyst_agent\user_data.db"
# 3. Save to SQLite
conn = sqlite3.connect(DB_path)
df.to_sql("data", conn, if_exists="replace", index=False)
conn.close()

print("\nData loaded into SQLite database successfully.")
