from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from database.models import db, User
from auth.utils import login_required

users_bp = Blueprint('users', __name__)

@users_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.role = request.form.get('role', user.role)
        db.session.commit()
        flash('Profil mis à jour avec succès.', 'success')
        return redirect(url_for('auth.profile'))

    return render_template('users/edit_profile.html', user=user)

@users_bp.route('/list')
@login_required
def list_users():
    users = User.query.all()
    return render_template('users/list_users.html', users=users)
