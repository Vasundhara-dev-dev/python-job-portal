import os
import re
import docx2txt
import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pyresparser import ResumeParser

# Download NLTK data if not done yet (only needed once)
import nltk
nltk.download('punkt')
nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

# Supported skills – this can be extended or loaded from a JSON file
SKILLS_DB = [
    'python', 'java', 'c++', 'html', 'css', 'javascript', 'sql',
    'react', 'nodejs', 'django', 'flask', 'tensorflow', 'keras',
    'machine learning', 'data science', 'deep learning',
    'nlp', 'cloud', 'aws', 'azure', 'docker', 'kubernetes', 'git'
]


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ''
    return text


def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)


def clean_text(text):
    # Lowercase and remove stopwords
    tokens = word_tokenize(text.lower())
    words = [word for word in tokens if word.isalpha() and word not in STOPWORDS]
    return words


def extract_skills(text_tokens):
    skills_found = set()
    text = " ".join(text_tokens)
    for skill in SKILLS_DB:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text):
            skills_found.add(skill)
    return list(skills_found)


def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-]{8,}\d', text)
    return match.group(0) if match else None


def parse_resume(file_path):
    """
    Main function to parse resume and return a dictionary
    """
    extension = os.path.splitext(file_path)[1].lower()
    
    if extension == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif extension in [".doc", ".docx"]:
        text = extract_text_from_docx(file_path)
    else:
        return {"error": "Unsupported file format"}

    tokens = clean_text(text)

    data = {
        "name": None,
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(tokens),
        "education": None,
        "experience": None,
        "raw_text": text[:1000]  # Limit for debugging/logging
    }

    # Optional: Try using pyresparser for better extraction (if it works)
    try:
        extracted = ResumeParser(file_path).get_extracted_data()
        data.update({
            "name": extracted.get("name"),
            "education": extracted.get("education"),
            "experience": extracted.get("experience")
        })
    except Exception as e:
        print("pyresparser failed:", e)

    return data
