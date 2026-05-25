from database.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
import jwt
import datetime

def register_user(username, password, email, role='user'):
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return False
    
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, email=email, role=role)
    db.session.add(new_user)
    db.session.commit()
    return True

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

def generate_jwt_token(user_id, username, role):
    payload = {
        'user_id': user_id,
        'username': username,
        'role': role,
    }
    token = jwt.encode(payload, current_app.config['JWT_SECRET'], algorithm='HS256')
    return token

def decode_jwt_token(token):
    payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=['HS256'])
    return payload
