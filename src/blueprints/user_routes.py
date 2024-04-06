# blueprints/user_routes.py
from flask import Blueprint, jsonify, current_app
from managements.user_management import UserManagement

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/users', methods=['GET'])
def list_users():
    db_path = current_app.config['dbPath']  # Accede directamente a la ruta de la base de datos desde la configuración actual
    user_manager = UserManagement(db_path)
    users = user_manager.list_all_users()
    return jsonify(users=users), 200
