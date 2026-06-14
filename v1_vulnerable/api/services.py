from database.models import User, Ticket

def get_all_users_data():
    # TODO SECURITY: Fuite d'informations - toutes les informations utilisateur sont exposées sans filtrage
    users = User.query.all()
    return [{"id": u.id, "username": u.username, "email": u.email, "role": u.role} for u in users]

def get_all_tickets_data():
    # TODO SECURITY: Fuite d'informations - toutes les informations de ticket sont exposées sans filtrage
    tickets = Ticket.query.all()
    return [{"id": t.id, "title": t.title, "content": t.content, "author_id": t.author_id, "status": t.status} for t in tickets]
