from groq import Groq
import os
from dotenv import load_dotenv
import re

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def auto_map_columns(sql, actual_columns):
    """
    Automatically map LLM-generated column names
    to actual dataset column names.
    """
    normalized_map = {
        col.lower().replace("_", ""): col
        for col in actual_columns
    }

    words = re.findall(r"[A-Za-z_]+", sql)

    for word in words:
        key = word.lower().replace("_", "")
        if key in normalized_map:
            sql = re.sub(rf"\b{word}\b", normalized_map[key], sql)

    return sql

def execute_with_retry(conn, sql, question, columns):
    cursor = conn.cursor()

    try:
        #  Apply column auto-mapping BEFORE execution
        sql = auto_map_columns(sql, columns)
        cursor.execute(sql)
        return cursor.fetchall(), sql

    except Exception as e:
        error_message = str(e)

        fix_prompt = f"""
You are fixing a SQLite query.

IMPORTANT RULES:
- Use ONLY column names from this list: {columns}
- Do NOT invent column names
- Do NOT use markdown
- Do NOT include explanations
- Return ONLY valid SQLite SQL

Broken SQL:
{sql}

Error:
{error_message}

Table name: data

Correct SQL:
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": fix_prompt}],
            temperature=0
        )
        fixed_sql = response.choices[0].message.content.strip()

        #  Remove markdown if LLM adds it
        fixed_sql = fixed_sql.replace("```sql", "").replace("```", "").strip()
        #  Apply column auto-mapping AGAIN
        fixed_sql = auto_map_columns(fixed_sql, columns)

        cursor.execute(fixed_sql)
        return cursor.fetchall(), fixed_sql
