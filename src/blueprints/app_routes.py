# blueprints/app_routes.py
from flask import Blueprint, jsonify, current_app
from managements.app_management import AppManagement

app_blueprint = Blueprint('apps', __name__)

@app_blueprint.route('/apps', methods=['GET'])
def list_all_apps():
    db_path = current_app.config['dbPath']  # Accede directamente a la ruta de la base de datos desde la configuración actual
    app_manager = AppManagement(db_path)
    apps = app_manager.list_all_apps()
    return jsonify({'apps': apps}), 200


