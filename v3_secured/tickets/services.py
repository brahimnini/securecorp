from database.models import db, Ticket, Comment
from flask import escape

def create_ticket_entry(title, content, author_id):
    # Correction: Échappement HTML pour prévenir le XSS stocké
    new_ticket = Ticket(title=escape(title), content=escape(content), author_id=author_id)
    db.session.add(new_ticket)
    db.session.commit()
    return new_ticket

def get_all_tickets():
    return Ticket.query.all()

def get_ticket_by_id(ticket_id):
    return Ticket.query.get(ticket_id)

def add_comment_to_ticket(ticket_id, content, author_id):
    # Correction: Échappement HTML pour prévenir le XSS stocké
    new_comment = Comment(ticket_id=ticket_id, content=escape(content), author_id=author_id)
    db.session.add(new_comment)
    db.session.commit()
    return new_comment

def get_comments_for_ticket(ticket_id):
    return Comment.query.filter_by(ticket_id=ticket_id).all()
