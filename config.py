import os

class Config:
    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_dev_secret_key_here'
    DEBUG = True

    # Database Configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL') or
        'sqlite:///' + os.path.join(BASE_DIR, 'jobportal.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload Config
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads', 'resumes')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB file size limit
    ALLOWED_EXTENSIONS = {'pdf', 'docx'}

    # Resume Parser Settings (Optional)
    PARSER_LANGUAGE = 'en'
