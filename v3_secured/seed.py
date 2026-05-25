from app import create_app
from database.models import db, User, Ticket, Comment
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Création des utilisateurs
    admin = User(username='admin', password=generate_password_hash('Admin@123!'), email='admin@securecorp.com', role='admin')
    user1 = User(username='alice', password=generate_password_hash('Alice@123!'), email='alice@securecorp.com', role='user')
    user2 = User(username='bob', password=generate_password_hash('Bob@1234!'), email='bob@securecorp.com', role='user')
    
    db.session.add(admin)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Création des tickets
    ticket1 = Ticket(title="Problème d'accès VPN", content="Je n'arrive pas à me connecter au VPN depuis ce matin.", author_id=user1.id)
    ticket2 = Ticket(title="Demande de nouveau matériel", content="J'ai besoin d'un deuxième écran pour mon poste.", author_id=user2.id)
    
    db.session.add(ticket1)
    db.session.add(ticket2)
    db.session.commit()

    # Création des commentaires
    comment1 = Comment(content="As-tu essayé de redémarrer ton client VPN ?", ticket_id=ticket1.id, author_id=admin.id)
    
    db.session.add(comment1)
    db.session.commit()

    print("Données de démonstration créées avec succès pour la Version 3.")
