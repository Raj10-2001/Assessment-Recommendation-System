
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
![image](https://github.com/user-attachments/assets/6718f8ac-a7ee-4f19-a81b-a99c97657782)

 *Recommended Assessment List 1*  
![image](https://github.com/user-attachments/assets/ef530903-0f3b-4f9f-85a0-3a814fe6fc3a)

 *Job Description Input 2*  
![image](https://github.com/user-attachments/assets/7bb1b149-6ced-41fc-9ed7-a7e3298ccd16)

 *Recommended Assessment List 2*  

![image](https://github.com/user-attachments/assets/46f58f11-0535-442c-997a-314beb470770)

---

##  Tech Stack  

- *Python*  
- *Flask*  
- *BeautifulSoup* (for scraping SHL catalog)  
- *spaCy* (for NLP keyword extraction)  
- *Scikit-learn* (for TF-IDF + cosine similarity)  
- *HTML/CSS* (for simple frontend UI)  

---
