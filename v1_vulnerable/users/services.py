from database.models import db, User

def get_user_by_id(user_id):
    # TODO SECURITY: IDOR - L\"ID utilisateur est directement utilisé sans vérification d\"autorisation
    return User.query.get(user_id)

def update_user_profile(user_id, username, email, role):
    user = User.query.get(user_id)
    if user:
        # TODO SECURITY: Validation utilisateur insuffisante - pas de validation des entrées
        user.username = username
        user.email = email
        # TODO SECURITY: Mauvais contrôle RBAC - un utilisateur peut changer son propre rôle
        user.role = role
        db.session.commit()
        return True
    return False
