from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from database.models import db, Ticket, Comment, User
from auth.utils import login_required

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_ticket():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author_id = session['user_id']

        new_ticket = Ticket(title=title, content=content, author_id=author_id)
        db.session.add(new_ticket)
        db.session.commit()
        flash('Ticket créé avec succès.', 'success')
        return redirect(url_for('tickets.list_tickets'))
    return render_template('tickets/create_ticket.html')

@tickets_bp.route('/list')
@login_required
def list_tickets():
    tickets = Ticket.query.all()
    return render_template('tickets/list_tickets.html', tickets=tickets)

@tickets_bp.route('/view/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def view_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    comments = Comment.query.filter_by(ticket_id=ticket_id).all()

    if request.method == 'POST':
        comment_content = request.form['comment_content']
        author_id = session['user_id']
        new_comment = Comment(content=comment_content, ticket_id=ticket_id, author_id=author_id)
        db.session.add(new_comment)
        db.session.commit()
        flash('Commentaire ajouté.', 'success')
        return redirect(url_for('tickets.view_ticket', ticket_id=ticket_id))

    return render_template('tickets/view_ticket.html', ticket=ticket, comments=comments)

@tickets_bp.route('/export_csv')
@login_required
def export_csv():
    from io import StringIO
    import csv
    
    si = StringIO()
    cw = csv.writer(si)
    
    tickets = Ticket.query.all()
    cw.writerow(['ID', 'Title', 'Content', 'Author ID', 'Status', 'Created At'])
    for ticket in tickets:
        cw.writerow([ticket.id, ticket.title, ticket.content, ticket.author_id, ticket.status, ticket.created_at])
    
    output = si.getvalue()
    return render_template('debug_output.html', output=output, filename='tickets.csv')

@tickets_bp.route('/export_json')
@login_required
def export_json():
    import json
    
    tickets = Ticket.query.all()
    tickets_data = []
    for ticket in tickets:
        tickets_data.append({
            'id': ticket.id,
            'title': ticket.title,
            'content': ticket.content,
            'author_id': ticket.author_id,
            'status': ticket.status,
            'created_at': str(ticket.created_at)
        })
    
    output = json.dumps(tickets_data, indent=4)
    return render_template('debug_output.html', output=output, filename='tickets.json')
