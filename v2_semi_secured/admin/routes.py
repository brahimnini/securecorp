from flask import Blueprint, render_template, redirect, url_for, flash, session, abort
from database.models import User, Ticket, Document
from admin.services import get_all_users, delete_user_by_id, get_all_tickets, get_all_documents
from auth.utils import role_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@role_required('admin')
def admin_dashboard():
    users = get_all_users()
    tickets = get_all_tickets()
    documents = get_all_documents()
    return render_template('admin/dashboard.html', users=users, tickets=tickets, documents=documents)

@admin_bp.route('/users')
@role_required('admin')
def manage_users():
    users = get_all_users()
    return render_template('admin/users.html', users=users)

@admin_bp.route('/user/delete/<int:user_id>', methods=['POST'])
@role_required('admin')
def delete_user(user_id):
    if delete_user_by_id(user_id, session['user_id']):
        flash('Utilisateur supprimé avec succès.', 'success')
    else:
        flash("Erreur lors de la suppression de l'utilisateur ou autorisation insuffisante.", 'danger')
    return redirect(url_for('admin.manage_users'))

@admin_bp.route('/tickets')
@role_required('admin')
def manage_tickets():
    tickets = get_all_tickets()
    return render_template('admin/tickets.html', tickets=tickets)

@admin_bp.route('/documents')
@role_required('admin')
def manage_documents():
    documents = get_all_documents()
    return render_template('admin/documents.html', documents=documents)
