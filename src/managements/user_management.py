# managements/user_management.py
import os
import json
import sqlite3

class UserManagement:
    def __init__(self, db_path):
        self.db_path = db_path

    def load_config(self, config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Archivo de configuración no encontrado: {config_path}")

        with open(config_path) as config_file:
            try:
                config = json.load(config_file)
                return config
            except json.JSONDecodeError:
                raise ValueError(f"Error al parsear el archivo de configuración: {config_path}")

    def list_all_users(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Accesos")
        users = cursor.fetchall()
        conn.close()
        return users

    def insert_user(self, usuario, clave, App, habilitado):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Accesos (usuario, clave, App, habilitado) VALUES (?, ?, ?, ?)", (usuario, clave, App, habilitado))
        conn.commit()
        conn.close()

    def delete_user(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Accesos WHERE idUnico=?", (user_id,))
        conn.commit()
        conn.close()

    def update_user(self, user_id, new_values):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE Accesos SET usuario=?, clave=?, App=?, habilitado=? WHERE idUnico=?", (*new_values, user_id))
        conn.commit()
        conn.close()
        
    def validate_user(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Accesos WHERE usuario=? AND clave=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None
