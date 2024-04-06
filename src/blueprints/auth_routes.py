# blueprints/auth_routes.py
from flask import Blueprint, jsonify, request, current_app
from managements.token_management import TokenManagement
from managements.user_management import UserManagement

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/generate_token', methods=['POST'])
def generate_token_route():
    config = current_app.config  # Obtener el diccionario de configuración desde la aplicación Flask
    # Inicializar TokenManagement con el diccionario de configuración
    token_manager = TokenManagement(config)
    
    # Obtener los datos del cuerpo de la solicitud
    data = request.get_json()

    # Validar que se hayan proporcionado el nombre de usuario y la contraseña
    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Nombre de usuario y/o contraseña no proporcionados'}), 400

    secret_key, expiration_hours = token_manager.get_secret_key()

    # Obtener el objeto UserManagement y validar el usuario
    user_manager = UserManagement(current_app.config['Paths']['dbPath'])
    username = data['username']
    password = data['password']
    if not user_manager.validate_user(username, password):
        return jsonify({'error': 'Usuario no válido'}), 401

    # Generar el token JWT
    token = token_manager.generate_token(data)

    # Retornar el token generado
    return jsonify({'token': token}), 200
