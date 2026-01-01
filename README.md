#🤖 Autonomous AI Data Analyst Agent

An AI-powered data analysis system that allows users to upload a CSV dataset once and ask multiple natural language questions, automatically generating SQL queries, insights, explanations, and visualizations.

This project demonstrates LLM-powered agents, Text-to-SQL, auto-error correction, and dynamic data visualization — similar to real-world BI tools.

# Key Features

 Upload CSV Dataset Once

 Ask Questions in Natural Language

 Automatic Text-to-SQL Generation

🛠Self-Healing SQL (Auto Error Fixing)

 Column Auto-Mapping (Schema Adaptation)

 Dynamic Visualizations (Bar & Line Charts)

 Multi-Metric Charts Support

 SQL Query Display

 Human-Readable Explanation

 Clear & Reload Dataset

 Modern Web UI (HTML, CSS, Chart.js)

#Project Architecture
ai_data_analyst_agent/
│
├── agent/
│   ├── main_logic.py        # Core agent logic
│   ├── text_to_sql.py       # Natural Language → SQL
│   ├── sql_executor.py      # SQL execution + auto-fix + column mapping
│   ├── explain_result.py    # Result explanation using LLM
│
├── web/
│   ├── app.py               # Flask backend
│   ├── templates/
│   │   └── index.html       # UI
│   └── static/
│       └── style.css        # Styling
│
├── user_data.db             # SQLite database (auto-created)
├── requirements.txt
└── README.md

# How It Works (High Level)

User uploads a CSV dataset

Data is stored in SQLite

User asks a natural language question

LLM converts question → SQL

SQL is executed safely

If SQL fails:

Agent auto-fixes SQL

Applies column auto-mapping

Results are:

Displayed as table

Explained in simple language

Visualized automatically if numeric

#Visualization Logic

Single Metric → Bar / Line Chart

Multiple Metrics → Grouped / Multi-Line Charts

Charts are shown only when meaningful

Built using Chart.js

🧩 Column Auto-Mapping (Important Feature)

The agent automatically adapts to different dataset schemas.

Example:

OrderDate → ORDERDATE
order date → ORDERDATE
Sales → SALES


This prevents:

SQL crashes

LLM hallucination issues

Schema mismatch errors

🛠 Technologies Used

Python 3.10

Flask

SQLite

Pandas

Groq LLM (LLama 3)

Chart.js

HTML & CSS

# Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-url>
cd ai_data_analyst_agent

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here

5️⃣ Run Application
python -m web.app


Open browser:

http://127.0.0.1:5000

# Sample Questions

# Graph Appears:

total sales by year
total sales by product line
total sales by country
sales trend by year
total sales and quantity by year


# Graph Not Needed:

total sales
show first 5 rows
top customer

# Why This Project Is Strong for Interviews

Demonstrates AI agents

Handles LLM errors automatically

Shows real-world data engineering problems

Combines AI + Backend + Visualization

Similar to tools like Power BI / Tableau (AI-powered)

# Interview Explanation (Short)

“I built an autonomous AI data analyst that converts natural language questions into SQL, automatically fixes errors, adapts to different schemas, and visualizes results dynamically.”

# Future Enhancements

KPI cards (Total Sales, Best Product)

Download charts as images

Query history (chat-style)

Support for Excel & JSON

Authentication & multi-user support

# Author

Sanjay Kumar Saini
Python | ML | AI Agents | Data Science
