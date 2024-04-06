# main.py
import os
import json
from flask import Flask
from blueprints.auth_routes import auth_blueprint
from blueprints.user_routes import user_blueprint
from blueprints.app_routes import app_blueprint

app = Flask(__name__)
# Registrar los blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(app_blueprint)

def create_app():
    # Configurar rutas del gateway
    return app

def load_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Archivo de configuración no encontrado: {config_path}")

    with open(config_path) as config_file:
        try:
            config = json.load(config_file)
            return config
        except json.JSONDecodeError:
            raise ValueError(f"Error al parsear el archivo de configuración: {config_path}")

if __name__ == "__main__":
    CONFIG_PATH = 'src/config/config.json'
    config = load_config(CONFIG_PATH)
    db_path = config['Paths']['dbPath']  # Obtener la ruta de la base de datos desde la configuración
    try:
        gateway_config = config.get('Gateway', {})
        host = gateway_config.get('host', '127.0.0.1')
        port = gateway_config.get('port', 5000)
        debug = gateway_config.get('debug', True)

        app = create_app()
        app.config['dbPath'] = db_path  # Agregar la ruta de la base de datos a la configuración de la aplicación
        app.config.update(config)  # Agregar el diccionario de configuración completo a la aplicación

        # Asegúrate de pasar la aplicación Flask al registrar las rutas en los blueprints
        app.register_blueprint(auth_blueprint, name='auth_blueprint', app=app)
        app.run(host=host, port=port, debug=debug)
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")

