import re
from difflib import get_close_matches
from typing import List, Tuple

# Common skill keywords (can be extended or loaded from a config/database)
KNOWN_SKILLS = [
    "Python", "Java", "C++", "JavaScript", "HTML", "CSS", "SQL", "React", "Node.js",
    "Flask", "Django", "TensorFlow", "Keras", "Machine Learning", "Data Analysis",
    "Data Science", "Pandas", "NumPy", "Scikit-learn", "Git", "Docker", "Kubernetes",
    "AWS", "Azure", "Linux", "REST API", "Firebase"
]

def validate_email(email: str) -> bool:
    """Validate email address format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(pattern, email) is not None

def normalize_skills(skills_text: str) -> List[str]:
    """
    Normalize skills from extracted resume text.
    Returns a cleaned list of skills (e.g., removing duplicates and formatting).
    """
    if not skills_text:
        return []

    skill_list = re.split(r'[,\n;]', skills_text)
    cleaned = [s.strip().title() for s in skill_list if s.strip()]
    return list(set(cleaned))  # remove duplicates

def match_skills(resume_skills: List[str], job_required_skills: List[str]) -> Tuple[float, List[str]]:
    """
    Compare resume skills against required job skills.
    Returns (match percentage, missing_skills).
    """
    matched_skills = [skill for skill in job_required_skills if skill in resume_skills]
    missing_skills = [skill for skill in job_required_skills if skill not in resume_skills]

    match_percent = round(len(matched_skills) / len(job_required_skills) * 100, 2) if job_required_skills else 0
    return match_percent, missing_skills

def suggest_skills(missing_skills: List[str]) -> List[str]:
    """
    Suggest learning resources or alternate skills based on missing ones.
    (Stub version: just suggests to 'learn XYZ' for now)
    """
    suggestions = []
    for skill in missing_skills:
        suggestions.append(f"Consider improving your {skill} skills via online platforms like Coursera, Udemy, or LinkedIn Learning.")
    return suggestions

def extract_keywords(text: str, known_keywords: List[str] = KNOWN_SKILLS) -> List[str]:
    """
    Extract known keywords from raw text using fuzzy matching.
    Returns the best matches from known keywords.
    """
    found_skills = []
    words = set(re.findall(r'\b\w+\b', text))
    for word in words:
        matches = get_close_matches(word.title(), known_keywords, n=1, cutoff=0.8)
        if matches:
            found_skills.append(matches[0])
    return list(set(found_skills))
