from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

import os

if os.path.isfile(".env"):
    load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)