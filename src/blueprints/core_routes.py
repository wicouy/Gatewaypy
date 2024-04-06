# blueprints/core_routes.py
from flask import Blueprint, request, jsonify, current_app
from managements.core_management import CoreManagement

core_blueprint = Blueprint('core', __name__)

@core_blueprint.route('/api/core', methods=['POST'])
def core_route():
    # Obtener los datos de la solicitud
    request_data = request.json
    
    # Crear una instancia del manejador del core
    core_manager = CoreManagement(current_app.config['dbPath'])
    
    # Redirigir la solicitud al backend seleccionado
    response_data = core_manager.redirect_request(request_data)
    
    # Devolver la respuesta del backend al cliente
    return jsonify(response_data), 200
