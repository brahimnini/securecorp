from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from database.models import db, User
from auth.utils import login_required, role_required, is_owner_or_admin
import re
from markupsafe import escape

users_bp = Blueprint('users', __name__)

@users_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)

    if not user or not is_owner_or_admin(user_id):
        flash('Accès non autorisé.', 'danger')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        if not re.match(r"^[a-zA-Z0-9_]{3,20}$", username):
            flash("Nom d'utilisateur invalide.", 'danger')
            return render_template('users/edit_profile.html', user=user)
        
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            flash("Format d'email invalide.", 'danger')
            return render_template('users/edit_profile.html', user=user)

        user.username = escape(username)
        user.email = escape(email)
        db.session.commit()
        flash('Profil mis à jour avec succès.', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('users/edit_profile.html', user=user)

@users_bp.route('/list')
@role_required('admin')
def list_users():
    users = User.query.all()
    return render_template('users/list_users.html', users=users)
