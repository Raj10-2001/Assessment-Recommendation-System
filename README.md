
# SHL Assessment Recommendation System  

This project is a smart recommendation engine that helps hiring managers find the most relevant SHL assessments for a given job description. Instead of manually browsing the SHL product catalog, this tool takes natural language input and returns tailored recommendations — fast, easy, and efficient.  

---

## How It Works  

*Input:* Natural language job description or role profile  
*Processing:* NLP-based keyword extraction and TF-IDF similarity scoring  
*Output:* A list of the *top 10 most relevant SHL assessments* with all required attributes:  

- *Assessment Name* (with direct link to SHL catalog)  
- *Remote Testing Support* (Yes/No)  
- *Adaptive/IRT Support* (Yes/No)  
- *Duration*  
- *Test Type*  

###  Example Inputs & Outputs  

 *Job Description Input 1*
 ![image](https://github.com/user-attachments/assets/db883ef7-1348-45b3-b832-05534354355c)
 *Recommended Assessment List 1*  
![image](https://github.com/user-attachments/assets/b24e619a-c37e-4060-bcb7-81849f729ff6)
 *Job Description Input 2*  
 ![image](https://github.com/user-attachments/assets/30e4a317-25cb-44a4-b88c-f6c3b62ce3ce)
 *Recommended Assessment List 2*  
![image](https://github.com/user-attachments/assets/f5e9e380-faaf-4038-9c3a-6ac983251cf4)
---

##  Tech Stack  

- *Python*  
- *Flask*  
- *BeautifulSoup* (for scraping SHL catalog)  
- *spaCy* (for NLP keyword extraction)  
- *Scikit-learn* (for TF-IDF + cosine similarity)  
- *HTML/CSS* (for simple frontend UI)  

---
