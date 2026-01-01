import os
import pandas as pd
import sqlite3
from flask import Flask, redirect, render_template, request , session
from agent.main_logic import run_agent

UPLOAD_FOLDER = "uploads"
#DB_PATH = "database/user_data.db"

app = Flask(__name__)
app.secret_key = "ai_data_analyst_secret_key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/clear", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    message = None

    if request.method == "POST":
        file = request.files.get("file")
        question = request.form.get("question")

        #  If user uploads file for the first time
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            df = pd.read_csv(filepath)
            df.columns = [c.strip().upper().replace(" ", "_").replace("-", "_") for c in df.columns]
            conn = sqlite3.connect("user_data.db")
            df.to_sql("data", conn, if_exists="replace", index=False)
            conn.close()

            session["data_loaded"] = True
            message = "Dataset uploaded successfully."

        #  If user asks question without uploading data
        if question and not session.get("data_loaded"):
            message = "Please upload a dataset first."

        #  If data already loaded, allow unlimited questions
        if question and session.get("data_loaded"):
            response = run_agent(question)

    return render_template("index.html", response=response, message=message)


if __name__ == "__main__":
    app.run(debug=True)
