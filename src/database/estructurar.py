import sqlite3

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
                        habilitado bool
                     )''')
        # Insertar un usuario Admin en la tabla Accesos si no existe
    cursor.execute('''INSERT INTO Accesos (usuario, clave, App, habilitado) VALUES ('master', '123','Todas',1)''')


    # Crear la tabla Aplicaciones
    cursor.execute('''CREATE TABLE IF NOT EXISTS Aplicaciones (
                        idUnicoApp INTEGER PRIMARY KEY,
                        nombreApp TEXT,
                        urlBackend TEXT,
                        infoAdicional TEXT,
                        habilitado bool
                     )''')

    # Crear la tabla Tokens
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tokens (
                        idUnico INTEGER PRIMARY KEY,
                        idUnicoApp INTEGER,
                        fechaCreacion TEXT,
                        fechaExpiracion TEXT,
                        usuarioSolicitante TEXT,
                        FOREIGN KEY (idUnicoApp) REFERENCES Aplicaciones (idUnicoApp)
                     )''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Ruta de la base de datos
    db_path = 'src/database/mydb.db'

    # Crear la base de datos
    create_database(db_path)
    print("Base de datos creada exitosamente.")
