from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from auth.services import register_user, authenticate_user, generate_jwt_token, decode_jwt_token
from database.models import User
import jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = 'user'

        if register_user(username, password, email, role):
            flash('Inscription réussie. Veuillez vous connecter.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash("Erreur lors de l'inscription. Veuillez réessayer.", 'danger')

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = authenticate_user(username, password)
        if user:
            token = generate_jwt_token(user.id, user.username, user.role)
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            session['jwt_token'] = token
            flash('Connexion réussie.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash("Nom d'utilisateur ou mot de passe incorrect.", 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('role', None)
    session.pop('jwt_token', None)
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Veuillez vous connecter pour voir votre profil.', 'warning')
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['user_id'])
    if not user:
        flash('Utilisateur non trouvé.', 'danger')
        return redirect(url_for('auth.login'))

    return render_template('auth/profile.html', user=user)

@auth_bp.route('/jwt_info')
def jwt_info():
    token = session.get('jwt_token')
    if not token:
        flash('Aucun JWT trouvé.', 'warning')
        return redirect(url_for('auth.login'))
    
    try:
        decoded_payload = decode_jwt_token(token)
        flash(f'JWT décodé: {decoded_payload}' , 'info')
    except jwt.ExpiredSignatureError:
        flash('Le token JWT a expiré.', 'danger')
    except jwt.InvalidTokenError:
        flash('Token JWT invalide.', 'danger')
    
    return redirect(url_for('dashboard'))
