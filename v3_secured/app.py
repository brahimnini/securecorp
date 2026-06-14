from flask import Flask, render_template, redirect, url_for, flash, request, session
from config import Config
from database.models import db, User, Ticket, Comment, Document
from auth.routes import auth_bp
from admin.routes import admin_bp
from api.routes import api_bp
from tickets.routes import tickets_bp
from users.routes import users_bp
import os
import logging
from logging.handlers import RotatingFileHandler
from markupsafe import escape
from flask_wtf.csrf import CSRFProtect

# Configuration du logging sécurisé
if not os.path.exists('logs'):
    os.makedirs('logs')
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
log_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
log_handler.setFormatter(log_formatter)
log_handler.setLevel(logging.INFO)

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.config.from_object(Config)

    # Ajout du handler de log à l'application
    app.logger.addHandler(log_handler)
    app.logger.setLevel(logging.INFO)

    db.init_app(app)

    # Enregistrement des blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(tickets_bp, url_prefix='/tickets')
    app.register_blueprint(users_bp, url_prefix='/users')

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        name = request.args.get('name', 'Guest')
        return render_template('index.html', name=escape(name))

    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            flash('Veuillez vous connecter pour accéder au tableau de bord.', 'warning')
            return redirect(url_for('auth.login'))
        
        user = User.query.get(session['user_id'])
        if not user:
            flash('Utilisateur non trouvé.', 'danger')
            return redirect(url_for('auth.login'))

        app.logger.info(f"Accès au tableau de bord par {user.username}")
        return render_template('dashboard.html', user=user)

    @app.errorhandler(404)
    def page_not_found(e):
        app.logger.warning(f"Page non trouvée: {request.url}")
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        app.logger.error(f"Erreur interne du serveur: {e}", exc_info=True)
        return render_template('500.html'), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
