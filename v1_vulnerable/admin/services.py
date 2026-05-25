from database.models import db, User, Ticket, Document

def get_all_users():
    return User.query.all()

def delete_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

def get_all_tickets():
    return Ticket.query.all()

def get_all_documents():
    return Document.query.all()
