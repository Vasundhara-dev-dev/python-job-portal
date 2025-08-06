import json
from datetime import datetime

# Sample data for in-memory career guidance (can be replaced with DB or API later)
RECOMMENDED_CAREERS = {
    'Data Science': ['Python', 'Pandas', 'NumPy', 'Machine Learning', 'SQL'],
    'Web Development': ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js'],
    'Cloud Engineering': ['AWS', 'Docker', 'Kubernetes', 'Terraform'],
    'Cybersecurity': ['Networking', 'Linux', 'Penetration Testing', 'SIEM', 'Firewalls'],
    'Mobile Development': ['Java', 'Kotlin', 'Swift', 'Flutter'],
}

COURSE_SUGGESTIONS = {
    'Python': 'https://www.coursera.org/learn/python',
    'Pandas': 'https://www.datacamp.com/courses/pandas-foundations',
    'React': 'https://reactjs.org/docs/getting-started.html',
    'Docker': 'https://www.docker.com/101-tutorial/',
    'SQL': 'https://mode.com/sql-tutorial/',
    'Machine Learning': 'https://www.coursera.org/learn/machine-learning',
    'Kubernetes': 'https://kubernetes.io/docs/tutorials/',
    'JavaScript': 'https://javascript.info/',
    'AWS': 'https://aws.amazon.com/training/',
    'Cybersecurity': 'https://www.cybrary.it/catalog/cybersecurity/',
}


def identify_skill_gaps(user_skills, target_role_skills):
    """
    Returns a list of skills that are missing from the user's profile
    """
    return [skill for skill in target_role_skills if skill not in user_skills]


def recommend_career(user_skills):
    """
    Suggest the most suitable career path based on matched skills
    """
    match_scores = {}

    for career, required_skills in RECOMMENDED_CAREERS.items():
        matches = set(user_skills).intersection(set(required_skills))
        match_scores[career] = len(matches)

    # Return career path with the highest match
    best_career = max(match_scores, key=match_scores.get)
    return best_career, RECOMMENDED_CAREERS[best_career]


def suggest_courses(skill_gaps):
    """
    Return course links for the missing skills
    """
    suggestions = []
    for skill in skill_gaps:
        course = COURSE_SUGGESTIONS.get(skill)
        if course:
            suggestions.append({
                'skill': skill,
                'course_url': course
            })
    return suggestions


def generate_career_advice(user_skills):
    """
    Main function to generate full career advice:
    - Best role
    - Skill gaps
    - Recommended resources
    """
    best_role, required_skills = recommend_career(user_skills)
    missing_skills = identify_skill_gaps(user_skills, required_skills)
    courses = suggest_courses(missing_skills)

    advice = {
        'suggested_role': best_role,
        'missing_skills': missing_skills,
        'recommended_courses': courses,
        'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return advice


# Sample test (remove or comment in production)
if __name__ == "__main__":
    user_skills_sample = ['Python', 'HTML', 'CSS']
    advice = generate_career_advice(user_skills_sample)
    print(json.dumps(advice, indent=4))
