import sqlite3
import random
import string

def create_database(db_path):
    # Conectar a la base de datos (creará el archivo si no existe)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear la tabla Accesos
    cursor.execute('''CREATE TABLE IF NOT EXISTS Accesos (
                        idUnico INTEGER PRIMARY KEY,
                        usuario TEXT,
                        clave TEXT,
                        App TEXT,
                        habilitado BOOL
                     )''')
    # Insertar un usuario Admin en la tabla Accesos si no existe
    cursor.execute('''INSERT INTO Accesos (usuario, clave, App, habilitado) VALUES ('master', '123','Todas',1)''')

    # Crear la tabla Aplicaciones
    cursor.execute('''CREATE TABLE IF NOT EXISTS Aplicaciones (
                        idApp INTEGER PRIMARY KEY,
                        nombreApp TEXT,
                        urlBackend TEXT,
                        infoAdicional TEXT,
                        habilitado BOOL
                     )''')
    
    # Insertar 3 ejemplos de aplicaciones
    for i in range(3):
        nombre_app = f"test_App_{i + 1}"
        url_backend = f"http://backend{i + 1}.example.com"
        info_adicional = f"Información adicional para la {nombre_app}"
        habilitado = 1  # Selección aleatoria de habilitado/deshabilitado
        
        cursor.execute('''INSERT INTO Aplicaciones (nombreApp, urlBackend, infoAdicional, habilitado) 
                          VALUES (?, ?, ?, ?)''', (nombre_app, url_backend, info_adicional, habilitado))

    # Crear índice en la tabla Aplicaciones para el nombre de la aplicación
    cursor.execute('''CREATE INDEX IF NOT EXISTS idx_nombreApp ON Aplicaciones (nombreApp)''')

    # Crear la tabla para los Endpoints de las Aplicaciones
    cursor.execute('''CREATE TABLE IF NOT EXISTS AplicacionesEndpoints (
                        idUnicoAppEnd INTEGER PRIMARY KEY,
                        idApp INTEGER,
                        nombreEndpint TEXT,
                        metodoHttp TEXT,
                        tipoRespuesta TEXT,
                        requiereToken BOOL,
                        urlBackend TEXT,
                        puertoBackend INT,
                        infoAdicional TEXT,
                        habilitado BOOL,
                        FOREIGN KEY (idApp) REFERENCES Aplicaciones(idApp)
                     )''')
    
    # Generar 10 endpoints aleatorios y relacionarlos aleatoriamente con las aplicaciones
    for i in range(10):
        id_app = random.randint(1, 3)  # Seleccionar aleatoriamente una de las 3 aplicaciones
        nombre_endpoint = 'test_'+''.join(random.choices(string.ascii_lowercase, k=5))  # Generar un nombre de endpoint aleatorio
        metodo_http = random.choice(['GET', 'POST', 'PUT', 'DELETE'])  # Seleccionar aleatoriamente un método HTTP
        tipo_respuesta = random.choice(['JSON', 'XML', 'HTML'])  # Seleccionar aleatoriamente un tipo de respuesta
        requiere_token = random.choice([True, False])  # Selección aleatoria de si requiere token o no
        url_backend = f"http://backend{id_app}.example.com/{nombre_endpoint}"  # URL del backend basada en el nombre de la aplicación y el endpoint
        puerto_backend = random.randint(8000, 9000)  # Puerto aleatorio
        info_adicional = f"Información adicional para el endpoint {nombre_endpoint}"
        habilitado = random.choice([True, False])  # Selección aleatoria de habilitado/deshabilitado
        
        cursor.execute('''INSERT INTO AplicacionesEndpoints (idApp, nombreEndpint, metodoHttp, tipoRespuesta, requiereToken, urlBackend, puertoBackend, infoAdicional, habilitado)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                          (id_app, nombre_endpoint, metodo_http, tipo_respuesta, requiere_token, url_backend, puerto_backend, info_adicional, habilitado))

    # Crear índice en la tabla AplicacionesEndpoints para el nombre del endpoint
    cursor.execute('''CREATE INDEX IF NOT EXISTS idx_nombreEndpoint ON AplicacionesEndpoints (nombreEndpint)''')

    # Crear la vista para mostrar las aplicaciones y sus endpoints asociados
    cursor.execute('''CREATE VIEW IF NOT EXISTS AppsWithEndpoints AS
                      SELECT
                          A.idApp,
                          A.nombreApp AS AppName,
                          AE.idUnicoAppEnd AS EndpointID,
                          AE.nombreEndpint AS EndpointName,
                          AE.metodoHttp AS HttpMethod,
                          AE.tipoRespuesta AS ResponseType,
                          AE.requiereToken AS RequiresToken,
                          AE.urlBackend AS BackendURL,
                          AE.puertoBackend AS BackendPort,
                          AE.infoAdicional AS EndpointInfo
                      FROM
                          Aplicaciones A
                      LEFT JOIN
                          AplicacionesEndpoints AE ON A.idApp = AE.idApp;''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Ruta de la base de datos
    db_path = 'src/database/mydb.db'

    # Crear la base de datos
    create_database(db_path)
    print("Base de datos creada exitosamente.")
