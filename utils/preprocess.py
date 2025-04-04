import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(job_description):
    doc = nlp(job_description)
    keywords = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ"]]
    return list(set(keywords))  # Remove duplicates
