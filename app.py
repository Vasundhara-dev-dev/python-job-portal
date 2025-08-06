from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
import os
import json
from pyresparser import ResumeParser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dummy job data for matching
job_posts = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'company': 'TechCorp',
        'required_skills': 'Python, SQL, Data Analysis, Excel'
    },
    {
        'id': 2,
        'title': 'Machine Learning Engineer',
        'company': 'AIWorks',
        'required_skills': 'Python, Machine Learning, TensorFlow, Deep Learning'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'company': 'WebSolutions',
        'required_skills': 'HTML, CSS, JavaScript, React'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', user={'name': 'Test User'})

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        flash('No file part')
        return redirect(url_for('dashboard'))
    file = request.files['resume']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('dashboard'))

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Parse resume using pyresparser
    data = ResumeParser(filepath).get_extracted_data()
    session['resume_data'] = data

    return redirect(url_for('resume_feedback'))

@app.route('/resume_feedback')
def resume_feedback():
    data = session.get('resume_data')
    if not data:
        return redirect(url_for('dashboard'))

    resume_skills = data.get('skills', [])
    all_skills = [skill.strip().lower() for skill in resume_skills]

    matched_jobs = []
    for job in job_posts:
        job_skills = [s.strip().lower() for s in job['required_skills'].split(',')]
        common = set(all_skills).intersection(set(job_skills))
        match_score = int(len(common) / len(job_skills) * 100)
        matched_jobs.append({
            'title': job['title'],
            'company': job['company'],
            'skills': job['required_skills'],
            'match_score': match_score
        })

    # Skill gap analysis
    all_job_skills = set()
    for job in job_posts:
        all_job_skills.update(s.strip().lower() for s in job['required_skills'].split(','))
    skill_gaps = list(all_job_skills.difference(set(all_skills)))

    feedback = {
        'name': data.get('name'),
        'email': data.get('email'),
        'skills': all_skills,
        'skill_gaps': skill_gaps[:5],  # show top 5 gaps
        'recommendations': [f"Learn {skill.title()} to expand job opportunities." for skill in skill_gaps[:5]]
    }

    session['matched_jobs'] = matched_jobs
    return render_template('resume_feedback.html', feedback=feedback)

@app.route('/job_list')
def job_list():
    matched_jobs = session.get('matched_jobs', [])
    return render_template('job_list.html', matched_jobs=matched_jobs)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
