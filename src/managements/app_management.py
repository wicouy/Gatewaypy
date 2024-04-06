# managements/app_management.py
import sqlite3

class AppManagement:
    def __init__(self, db_path):
        self.db_path = db_path

    def list_all_apps(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Aplicaciones")
        apps = cursor.fetchall()
        conn.close()
        return apps

    def insert_app(self, nombre_app, url_backend, info_adicional, habilitado):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Aplicaciones (nombreApp, urlBackend, infoAdicional, habilitado) VALUES (?, ?, ?, ?)", (nombre_app, url_backend, info_adicional, habilitado))
        conn.commit()
        conn.close()

    def delete_app(self, app_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Aplicaciones WHERE idUnicoApp=?", (app_id,))
        conn.commit()
        conn.close()

    def update_app(self, app_id, new_values):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE Aplicaciones SET nombreApp=?, urlBackend=?, infoAdicional=?, habilitado=? WHERE idUnicoApp=?", (*new_values, app_id))
        conn.commit()
        conn.close()
