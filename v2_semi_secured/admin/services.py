from database.models import db, User, Ticket, Document

def get_all_users():
    return User.query.all()

def delete_user_by_id(user_id, current_user_id):
    user_to_delete = User.query.get(user_id)
    if user_to_delete and user_to_delete.id != current_user_id:
        db.session.delete(user_to_delete)
        db.session.commit()
        return True
    return False

def get_all_tickets():
    return Ticket.query.all()

def get_all_documents():
    return Document.query.all()
