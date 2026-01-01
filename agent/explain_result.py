from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_result(question, sql, result):
    prompt = f"""
You are a data analyst.

User question:
{question}

SQL Query:
{sql}

SQL Result:
{result}

Explain the result in simple business-friendly language.
Do NOT mention SQL.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
