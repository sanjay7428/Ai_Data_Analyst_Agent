import pandas as pd
import sqlite3
from agent.text_to_sql import generate_sql
from agent.explain_result import explain_result
from agent.sql_executor import execute_with_retry

# Load DB schema
conn = sqlite3.connect("user_data.db")
df = pd.read_sql("SELECT * FROM data LIMIT 1", conn)
columns = df.columns.tolist()

question = input("Ask a question about the data: ")

sql = generate_sql(question, columns)
print("\nGenerated SQL:")
print(sql)

result, final_sql = execute_with_retry(conn, sql, question, columns)

print("\nFinal SQL Used:")
print(final_sql)

print("\nResult:")
for row in result:
    print(row)

explanation = explain_result(question, sql, result)
print("\nExplanation:")
print(explanation)

conn.close()
