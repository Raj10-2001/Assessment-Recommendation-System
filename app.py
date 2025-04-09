from flask import Flask, render_template, request, jsonify
import pandas as pd
from utils.preprocess import extract_keywords
from utils.recommend import recommend_assessments

app = Flask(__name__)

# ✅ Web form (working)
@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    if request.method == "POST":
        job_desc = request.form["job_desc"]
        recommendations = recommend_assessments(job_desc)
    return render_template("index.html", recommendations=recommendations)

# ✅ Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

# ✅ JSON API (for external calls like Postman)
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    query = data.get("query")
    
    if not query:
        return jsonify({"error": "Missing 'query' in request"}), 400

    df = recommend_assessments(query)

    formatted = []
    for row in df:
        formatted.append({
            "url": row.get("url", "https://example.com"),
            "adaptive_support": row.get("adaptive_support", "No"),
            "description": row.get("description", "No description provided."),
            "duration": int(row.get("duration", 30)),
            "remote_support": row.get("remote_support", "Yes"),
            "test_type": row.get("test_type", ["General"])
        })

    return jsonify({"recommended_assessments": formatted}), 200

if __name__ == "__main__":
    app.run(debug=True)
