# 🧠 AI-Powered Job Portal with Resume Screening & Career Counseling

An intelligent web-based job portal that uses AI to streamline the recruitment process with **automated resume parsing**, **skill matching**, and **personalized career guidance** for students and job seekers.

---

## Features

- **User Authentication** (Candidate & Employer roles)
- **Resume Upload & Parsing** using AI
- **AI-based Resume Screening** and Skill Gap Analysis
- **Job Search & Applications**
- **Employer Dashboard**: Post jobs, screen candidates via AI
- **Career Counseling** with personalized advice and upskilling recommendations

---

## 🛠️ Tech Stack

| Layer           | Technology                               |
|----------------|-------------------------------------------|
| Frontend        | HTML5, CSS3, Bootstrap 5, Jinja2 Templates |
| Backend         | Python, Flask, SQLAlchemy                |
| Database        | SQLite (default), can be swapped with PostgreSQL |
| Resume Parsing  | `pyresparser`, `spaCy`, `pdfminer.six`   |
| ML/NLP Tools    | `scikit-learn`, `nltk`, `pandas`         |
| Environment     | `python-dotenv`, `Flask-WTF`             |

---
## 📁 Project Structure

job-portal/
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── README.md
├── static/
│ ├── css/
│ ├── js/
│ ├── img/
│ └── uploads/
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── resume_feedback.html
│ ├── job_list.html
│ ├── employer_dashboard.html
│ └── career_advice.html
└── utils/
├── resume_parser.py
├── job_matcher.py
├── career_counselor.py
└── helper.py

📌 Example Use Cases
✅ Upload your resume and get AI feedback instantly.

✅ Get job recommendations that match your skills.

✅ Employers can post jobs and filter candidates using AI.

✅ Students get personalized career advice and learning suggestions.

🤖 AI Features in Detail
Resume Parsing: Extract name, skills, education, experience.

Skill Matching: AI compares required vs. actual skills using NLP (TF-IDF + cosine similarity).

Career Counseling: Generates advice on missing skills and recommends relevant career paths or courses.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.
