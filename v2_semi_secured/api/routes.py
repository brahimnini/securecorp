from flask import Blueprint, jsonify, request, current_app, session
from auth.services import decode_jwt_token
from database.models import User, Ticket
from auth.utils import login_required, role_required

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
@role_required('admin')
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@api_bp.route('/user/<int:user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    user = User.query.get(user_id)
    if user and (user.id == session['user_id'] or session['role'] == 'admin'):
        return jsonify(user.to_dict())
    return jsonify({'message': 'Accès non autorisé ou utilisateur non trouvé'}), 403

@api_bp.route('/tickets', methods=['GET'])
@login_required
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'content': t.content, 'author_id': t.author_id} for t in tickets])

@api_bp.route('/ticket/<int:ticket_id>', methods=['GET'])
@login_required
def get_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if ticket:
        return jsonify({'id': ticket.id, 'title': ticket.title, 'content': ticket.content, 'author_id': ticket.author_id})
    return jsonify({'message': 'Ticket non trouvé'}), 404

@api_bp.route('/decode_jwt', methods=['POST'])
def decode_jwt():
    token = request.json.get('token')
    if not token:
        return jsonify({'message': 'Token manquant'}), 400
    try:
        decoded_payload = decode_jwt_token(token)
        return jsonify(decoded_payload)
    except Exception as e:
        return jsonify({'message': str(e)}), 400
