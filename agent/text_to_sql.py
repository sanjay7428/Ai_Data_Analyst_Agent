import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_sql(question, columns):
    prompt = f"""
You are an expert data analyst.

Table name: data
Columns: {columns}

Important:
- ORDERDATE is TEXT (not a date)
- use SUBSTR(ORDERDATE, 1, 4) to extract year

Rules:
- Generate ONLY a valid SQLite SQL query
- No explanation
- No markdown
- Use correct column names

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()
