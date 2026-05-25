import os

class Config:
    SECRET_KEY = "super-secret-key-123"
    JWT_SECRET = "jwt-secret-very-weak"
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database/securecorp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    DEBUG = True
