import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    """
    Clean and normalize text.
    """
    if not text:
        return ""
    # Lowercase, remove punctuation/numbers, extra spaces
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def compute_match_score(candidate_skills, job_skills):
    """
    Compute cosine similarity between candidate and job required skills.
    Returns match percentage (0 to 100).
    """
    # Preprocess both
    candidate_text = preprocess_text(' '.join(candidate_skills)) if isinstance(candidate_skills, list) else preprocess_text(candidate_skills)
    job_text = preprocess_text(' '.join(job_skills)) if isinstance(job_skills, list) else preprocess_text(job_skills)

    if not candidate_text or not job_text:
        return 0.0

    # Vectorize
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([candidate_text, job_text])
    
    # Compute cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity * 100, 2)

def match_candidate_to_jobs(candidate_skills, job_list):
    """
    Given a list of job dicts and candidate skills,
    return jobs with computed match score.
    
    job_list format:
    [
        {'title': 'Data Analyst', 'company': 'ABC Corp', 'required_skills': 'Python SQL Excel'},
        {'title': 'ML Engineer', 'company': 'XYZ Ltd', 'required_skills': 'Python Machine Learning Deep Learning'}
    ]
    """
    matched_jobs = []

    for job in job_list:
        score = compute_match_score(candidate_skills, job.get('required_skills', ''))
        job_with_score = job.copy()
        job_with_score['match_score'] = score
        matched_jobs.append(job_with_score)

    # Optional: sort by match score
    matched_jobs.sort(key=lambda x: x['match_score'], reverse=True)
    return matched_jobs
