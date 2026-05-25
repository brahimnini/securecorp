import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32).hex()
    JWT_SECRET = os.environ.get('JWT_SECRET') or os.urandom(32).hex()
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database/securecorp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    
    DEBUG = False
    TESTING = False
    
    SESSION_COOKIE_SECURE = False # Désactivé pour le test local HTTP
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
