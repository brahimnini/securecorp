from app import create_app
from database.models import db, User, Ticket, Comment, Document
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Création des utilisateurs
    admin = User(username='admin', password=generate_password_hash('admin123'), email='admin@securecorp.com', role='admin')
    user1 = User(username='alice', password=generate_password_hash('alice123'), email='alice@securecorp.com', role='user')
    user2 = User(username='bob', password=generate_password_hash('bob123'), email='bob@securecorp.com', role='user')
    
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

    # Création des documents
    doc1 = Document(
        filename="vpn_guide.pdf",
        original_name="Guide_VPN.pdf",
        owner_id=user1.id
    )

    doc2 = Document(
        filename="materiel_demande.docx",
        original_name="Demande_Materiel.docx",
        owner_id=user2.id
    )

    doc3 = Document(
        filename="procedure_admin.txt",
        original_name="Procedure_Admin.txt",
        owner_id=admin.id
    )

    db.session.add(doc1)
    db.session.add(doc2)
    db.session.add(doc3)
    db.session.commit()
    
    print("Données de démonstration créées avec succès pour la Version 1.")
