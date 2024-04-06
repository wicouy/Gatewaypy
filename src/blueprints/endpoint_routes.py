#blueprints/endpoint_routes.py
from flask import Blueprint, jsonify, request
from managements.endpoint_management import EndpointManagement

endpoint_blueprint = Blueprint('endpoint', __name__)

# Instanciar el objeto EndpointManagement
endpoint_management = EndpointManagement('src/database/mydb.db')

@endpoint_blueprint.route('/endpoints', methods=['GET'])
def get_all_endpoints():
    """
    Obtiene todos los endpoints de la base de datos y los devuelve como una lista JSON.
    """
    endpoints = endpoint_management.list_all_endpoints()
    return jsonify(endpoints)

@endpoint_blueprint.route('/api/endpoints', methods=['POST'])
def create_endpoint():
    """
    Crea un nuevo endpoint en la base de datos utilizando los datos proporcionados en la solicitud.
    """
    data = request.json
    nombre_endpoint = data.get('nombre_endpoint')
    metodo_http = data.get('metodo_http')
    tipo_respuesta = data.get('tipo_respuesta')
    requiere_token = data.get('requiere_token')
    url_backend = data.get('url_backend')
    puerto_backend = data.get('puerto_backend')
    info_adicional = data.get('info_adicional')
    habilitado = data.get('habilitado')

    endpoint_management.insert_endpoint(nombre_endpoint, metodo_http, tipo_respuesta, requiere_token, url_backend, puerto_backend, info_adicional, habilitado)
    return jsonify({'message': 'Endpoint created successfully'}), 201

@endpoint_blueprint.route('/api/endpoints/<int:endpoint_id>', methods=['DELETE'])
def delete_endpoint(endpoint_id):
    """
    Elimina un endpoint de la base de datos utilizando su ID.
    """
    endpoint_management.delete_endpoint(endpoint_id)
    return jsonify({'message': 'Endpoint deleted successfully'}), 200

@endpoint_blueprint.route('/api/endpoints/<int:endpoint_id>', methods=['PUT'])
def update_endpoint(endpoint_id):
    """
    Actualiza un endpoint de la base de datos utilizando su ID y los datos proporcionados en la solicitud.
    """
    data = request.json
    new_values = (
        data.get('nombre_endpoint'),
        data.get('metodo_http'),
        data.get('tipo_respuesta'),
        data.get('requiere_token'),
        data.get('url_backend'),
        data.get('puerto_backend'),
        data.get('info_adicional'),
        data.get('habilitado')
    )

    endpoint_management.update_endpoint(endpoint_id, new_values)
    return jsonify({'message': 'Endpoint updated successfully'}), 200
