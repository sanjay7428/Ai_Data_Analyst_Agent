import sqlite3
import pandas as pd
from agent.text_to_sql import generate_sql
from agent.sql_executor import execute_with_retry
from agent.explain_result import explain_result


def run_agent(question):
    conn = sqlite3.connect("user_data.db")

    # Get actual column names
    df = pd.read_sql("SELECT * FROM data LIMIT 1", conn)
    columns = df.columns.tolist()

    # Generate SQL
    sql = generate_sql(question, columns)

    # Execute SQL with retry & auto-fix
    result, final_sql = execute_with_retry(conn, sql, question, columns)

    # Generate explanation
    explanation = explain_result(question, final_sql, result)

    conn.close()

    # ===============================
    # FINAL VISUALIZATION LOGIC
    # ===============================
    chart_data = None

    if result and len(result) > 0 and len(result[0]) >= 2:
        labels = [str(row[0]) for row in result]
        datasets = []

        # Process numeric columns
        for col_idx in range(1, len(result[0])):
            values = []
            numeric = True

            for row in result:
                try:
                    val = row[col_idx]
                    if isinstance(val, str):
                        val = val.replace(",", "").strip()
                    values.append(float(val))
                except Exception:
                    numeric = False
                    break

            if numeric:
                datasets.append({
                    "label": f"Metric {col_idx}",
                    "data": values
                })

        # Create chart only if numeric metrics exist
        if datasets:
            chart_data = {
                "labels": labels,
                "datasets": datasets,
                "type": "line"
                if "year" in question.lower() or "trend" in question.lower()
                else "bar"
            }
    print("DEBUG CHART DATA SENT TO UI:")
    print(chart_data)
    return {
        "sql": final_sql,
        "result": result,
        "explanation": explanation,
        "chart": chart_data
    }
