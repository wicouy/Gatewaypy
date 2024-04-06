# managements/endpoint_management.py
import sqlite3

class EndpointManagement:
    def __init__(self, db_path):
        self.db_path = db_path

    def list_all_endpoints(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM AplicacionesEndpoints")
        endpoints = cursor.fetchall()
        conn.close()
        return endpoints

    def insert_endpoint(self, nombre_endpoint, metodo_http, tipo_respuesta, requiere_token, url_backend, puerto_backend, info_adicional, habilitado):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO AplicacionesEndpoints (nombreEndpint, metodoHttp, tipoRespuesta, requiereToken, urlBackend, puertoBackend, infoAdicional, habilitado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nombre_endpoint, metodo_http, tipo_respuesta, requiere_token, url_backend, puerto_backend, info_adicional, habilitado))
        conn.commit()
        conn.close()

    def delete_endpoint(self, endpoint_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM AplicacionesEndpoints WHERE idUnicoAppEnd=?", (endpoint_id,))
        conn.commit()
        conn.close()

    def update_endpoint(self, endpoint_id, new_values):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE AplicacionesEndpoints SET nombreEndpint=?, metodoHttp=?, tipoRespuesta=?, requiereToken=?, urlBackend=?, puertoBackend=?, infoAdicional=?, habilitado=? WHERE idUnicoAppEnd=?", (*new_values, endpoint_id))
        conn.commit()
        conn.close()
