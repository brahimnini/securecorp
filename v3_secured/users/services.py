from database.models import db, User

def get_user_by_id(user_id):
    return User.query.get(user_id)

def update_user_profile(user_id, username, email):
    user = User.query.get(user_id)
    if user:
        # Correction: Validation des entrées est faite au niveau des routes
        user.username = username
        user.email = email
        db.session.commit()
        return True
    return False
