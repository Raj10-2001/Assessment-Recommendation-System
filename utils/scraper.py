import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_shl_catalog_data():
    url = "https://www.shl.com/solutions/products/product-catalog/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    

    soup = BeautifulSoup(response.text, 'html.parser')
    

    product_cards = soup.select('.product-card') 
    
    assessments = []

    for card in product_cards:
        try:

            name = card.select_one('.product-name').text.strip()
            url = card.select_one('a')['href']
            

            remote_testing = "Yes" if "remote" in card.text.lower() else "No"
            adaptive_support = "Yes" if "adaptive" in card.text.lower() or "irt" in card.text.lower() else "No"
            

            duration_text = card.text
            duration_match = re.search(r'(\d+)\s*min', duration_text)
            duration = duration_match.group(1) if duration_match else "Not specified"
            

            test_type = "Cognitive" if "cognitive" in card.text.lower() else \
                        "Personality" if "personality" in card.text.lower() else \
                        "Behavioral" if "behavioral" in card.text.lower() else "Other"
            

            assessments.append({
                "Assessment Name": name,
                "URL": url,
                "Remote Testing Support": remote_testing,
                "Adaptive/IRT Support": adaptive_support,
                "Duration": duration,
                "Test Type": test_type
            })
        except Exception as e:
            print(f"Error processing card: {e}")
            continue
    
    return pd.DataFrame(assessments)



def create_synthetic_shl_dataset():

    assessments = [
        {
            "Assessment Name": "SHL Verify Interactive - Numerical Reasoning",
            "URL": "https://www.shl.com/solutions/products/verify-interactive-numerical-reasoning/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "Yes",
            "Duration": "25",
            "Test Type": "Cognitive"
        },
        {
            "Assessment Name": "SHL Verify Interactive - Verbal Reasoning",
            "URL": "https://www.shl.com/solutions/products/verify-interactive-verbal-reasoning/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "Yes",
            "Duration": "25",
            "Test Type": "Cognitive"
        },
        {
            "Assessment Name": "SHL Verify Interactive - Inductive Reasoning",
            "URL": "https://www.shl.com/solutions/products/verify-interactive-inductive-reasoning/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "Yes",
            "Duration": "25",
            "Test Type": "Cognitive"
        },
        {
            "Assessment Name": "SHL General Ability Test",
            "URL": "https://www.shl.com/solutions/products/general-ability-test/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "30",
            "Test Type": "Cognitive"
        },
        {
            "Assessment Name": "SHL Occupational Personality Questionnaire (OPQ)",
            "URL": "https://www.shl.com/solutions/products/occupational-personality-questionnaire/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "45",
            "Test Type": "Personality"
        },
        {
            "Assessment Name": "SHL Situational Judgement Test",
            "URL": "https://www.shl.com/solutions/products/situational-judgement-test/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "30",
            "Test Type": "Behavioral"
        },
        {
            "Assessment Name": "SHL Coding Assessment",
            "URL": "https://www.shl.com/solutions/products/coding-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "60",
            "Test Type": "Technical"
        },
        {
            "Assessment Name": "SHL Motivation Questionnaire (MQ)",
            "URL": "https://www.shl.com/solutions/products/motivation-questionnaire/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "25",
            "Test Type": "Personality"
        },
        {
            "Assessment Name": "SHL Sales Assessment",
            "URL": "https://www.shl.com/solutions/products/sales-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "40",
            "Test Type": "Behavioral"
        },
        {
            "Assessment Name": "SHL Leadership Assessment",
            "URL": "https://www.shl.com/solutions/products/leadership-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "Yes",
            "Duration": "45",
            "Test Type": "Behavioral"
        },
        {
            "Assessment Name": "SHL Microsoft Office Skills Test",
            "URL": "https://www.shl.com/solutions/products/microsoft-office-skills-test/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "35",
            "Test Type": "Technical"
        },
        {
            "Assessment Name": "SHL Customer Service Assessment",
            "URL": "https://www.shl.com/solutions/products/customer-service-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "30",
            "Test Type": "Behavioral"
        },
        {
            "Assessment Name": "SHL ADEPT-15 Personality Assessment",
            "URL": "https://www.shl.com/solutions/products/adept-15-personality-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "Yes",
            "Duration": "25",
            "Test Type": "Personality"
        },
        {
            "Assessment Name": "SHL Numerical Calculation Test",
            "URL": "https://www.shl.com/solutions/products/numerical-calculation-test/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "20",
            "Test Type": "Cognitive"
        },
        {
            "Assessment Name": "SHL Data Visualization Assessment",
            "URL": "https://www.shl.com/solutions/products/data-visualization-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "35",
            "Test Type": "Technical"
        },
        {
            "Assessment Name": "SHL Remote Work Assessment",
            "URL": "https://www.shl.com/solutions/products/remote-work-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "25",
            "Test Type": "Behavioral"
        },
        {
            "Assessment Name": "SHL Mechanical Comprehension Test",
            "URL": "https://www.shl.com/solutions/products/mechanical-comprehension-test/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "30",
            "Test Type": "Technical"
        },
        {
            "Assessment Name": "SHL Deductive Reasoning Test",
            "URL": "https://www.shl.com/solutions/products/deductive-reasoning-test/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "25",
            "Test Type": "Cognitive"
        },
        {
            "Assessment Name": "SHL Workplace Reliability Assessment",
            "URL": "https://www.shl.com/solutions/products/workplace-reliability-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "No",
            "Duration": "20",
            "Test Type": "Behavioral"
        },
        {
            "Assessment Name": "SHL Graduate Assessment",
            "URL": "https://www.shl.com/solutions/products/graduate-assessment/",
            "Remote Testing Support": "Yes",
            "Adaptive/IRT Support": "Yes",
            "Duration": "40",
            "Test Type": "Cognitive"
        }
    ]
    
    return pd.DataFrame(assessments)


df = create_synthetic_shl_dataset()


keywords = {
    "SHL Verify Interactive - Numerical Reasoning": ["numerical", "math", "quantitative", "analytics", "data analysis", "finance", "accounting", "engineering"],
    "SHL Verify Interactive - Verbal Reasoning": ["verbal", "language", "comprehension", "communication", "writing", "reading", "management"],
    "SHL Verify Interactive - Inductive Reasoning": ["inductive", "logic", "pattern recognition", "problem solving", "analytical thinking"],
    "SHL General Ability Test": ["general ability", "cognitive", "intelligence", "aptitude", "problem solving", "entry level"],
    "SHL Occupational Personality Questionnaire (OPQ)": ["personality", "traits", "work style", "team fit", "management", "leadership"],
    "SHL Situational Judgement Test": ["situational judgment", "decision making", "workplace scenarios", "people management"],
    "SHL Coding Assessment": ["coding", "programming", "software development", "IT", "computer science", "developer", "engineer"],
    "SHL Motivation Questionnaire (MQ)": ["motivation", "drive", "career goals", "engagement", "retention"],
    "SHL Sales Assessment": ["sales", "customer acquisition", "business development", "account management", "relationship building"],
    "SHL Leadership Assessment": ["leadership", "management", "executive", "team lead", "director", "strategic thinking"],
    "SHL Microsoft Office Skills Test": ["Microsoft Office", "Excel", "Word", "PowerPoint", "admin", "clerical", "office support"],
    "SHL Customer Service Assessment": ["customer service", "support", "customer experience", "help desk", "call center"],
    "SHL ADEPT-15 Personality Assessment": ["personality", "workplace behavior", "team fit", "cultural fit"],
    "SHL Numerical Calculation Test": ["calculation", "arithmetic", "data entry", "accounting", "finance", "bookkeeping"],
    "SHL Data Visualization Assessment": ["data visualization", "analytics", "business intelligence", "reporting", "dashboards"],
    "SHL Remote Work Assessment": ["remote work", "work from home", "virtual team", "distributed workforce"],
    "SHL Mechanical Comprehension Test": ["mechanical", "technical", "engineering", "manufacturing", "maintenance"],
    "SHL Deductive Reasoning Test": ["deductive reasoning", "logic", "critical thinking", "analysis", "problem solving"],
    "SHL Workplace Reliability Assessment": ["reliability", "attendance", "dependability", "work ethic", "entry level"],
    "SHL Graduate Assessment": ["graduate", "entry level", "new hire", "campus recruiting", "university"]
}


df["Keywords"] = df["Assessment Name"].map(lambda x: keywords.get(x, []))


print(df.head())


df.to_csv("data/shl_assessments.csv", index=False)


def recommend_assessments(query, df, max_recommendations=10):
    query = query.lower()
    scores = []
    
    for idx, row in df.iterrows():
        score = 0
        

        for keyword in row["Keywords"]:
            if keyword.lower() in query:
                score += 1
        

        if any(word.lower() in query for word in row["Assessment Name"].lower().split()):
            score += 0.5
            

        if row["Test Type"].lower() in query:
            score += 0.5
            
        scores.append((idx, score))
    

    top_indices = [idx for idx, score in sorted(scores, key=lambda x: x[1], reverse=True)[:max_recommendations] if score > 0]
    
    if not top_indices:

        if "coding" in query or "programming" in query or "technical" in query:
            return df[df["Test Type"] == "Technical"].head(max_recommendations)
        elif "personality" in query or "behavior" in query:
            return df[df["Test Type"] == "Personality"].head(max_recommendations)
        elif "cognitive" in query or "reasoning" in query or "intelligence" in query:
            return df[df["Test Type"] == "Cognitive"].head(max_recommendations)
        else:

            return df.sample(min(max_recommendations, len(df)))
    
    return df.iloc[top_indices]


example_query = "We need an assessment for a software developer position that tests coding skills and problem-solving abilities"
recommendations = recommend_assessments(example_query, df)
print("\nRecommendations for:", example_query)
print(recommendations[["Assessment Name", "URL", "Remote Testing Support", "Adaptive/IRT Support", "Duration", "Test Type"]])