from flask import Flask, request, render_template
import pandas as pd
import joblib
from utils.preprocess import extract_keywords
from utils.recommend import recommend_assessments

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = None
    if request.method == "POST":
        job_desc = request.form["job_desc"]
        recommendations = recommend_assessments(job_desc).to_dict(orient="records")
    
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
