from flask import Blueprint, render_template, redirect, url_for, flash, session, abort
from database.models import User, Ticket, Document
from admin.services import get_all_users, delete_user_by_id, get_all_tickets, get_all_documents
from functools import wraps

admin_bp = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'role' not in session or session['role'] != 'admin':
            flash('Accès non autorisé.', 'danger')
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/dashboard')
@admin_required
def admin_dashboard():
    users = get_all_users()
    tickets = get_all_tickets()
    documents = get_all_documents()
    return render_template('admin/dashboard.html', users=users, tickets=tickets, documents=documents)

@admin_bp.route('/users')
@admin_required
def manage_users():
    users = get_all_users()
    return render_template('admin/users.html', users=users)

@admin_bp.route('/user/delete/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    if delete_user_by_id(user_id):
        flash('Utilisateur supprimé avec succès.', 'success')
    else:
        flash("Erreur lors de la suppression de l'utilisateur.", 'danger')
    return redirect(url_for('admin.manage_users'))

@admin_bp.route('/tickets')
@admin_required
def manage_tickets():
    tickets = get_all_tickets()
    return render_template('admin/tickets.html', tickets=tickets)

@admin_bp.route('/documents')
@admin_required
def manage_documents():
    documents = get_all_documents()
    return render_template('admin/documents.html', documents=documents)
