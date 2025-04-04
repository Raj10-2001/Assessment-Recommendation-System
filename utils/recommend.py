import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.preprocess import extract_keywords
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/shl_assessments.csv")

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Assessment Name"] + " " + df["Test Type"])
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

def recommend_assessments(job_desc):
    job_keywords = " ".join(extract_keywords(job_desc))
    job_vector = vectorizer.transform([job_keywords])
    
    similarity_scores = cosine_similarity(job_vector, tfidf_matrix)[0]
    top_indices = similarity_scores.argsort()[-10:][::-1]
    
    return df.iloc[top_indices][["Assessment Name", "URL", "Remote Testing Support", "Adaptive/IRT Support", "Duration", "Test Type"]]

