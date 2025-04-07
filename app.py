from flask import Flask, render_template, request, jsonify
import pandas as pd
from utils.preprocess import extract_keywords
from utils.recommendation import recommend_assessments

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    if request.method == "POST":
        job_desc = request.form["job_description"]
        recommendations = recommend_assessments(job_desc)
        recommendations = recommendations.to_dict(orient="records")
    return render_template("index.html", recommendations=recommendations)


@app.route("/api/query", methods=["POST"])
def api_query():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    job_desc = data["text"]
    recommendations = recommend_assessments(job_desc).to_dict(orient="records")
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
