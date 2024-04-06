# Gatewaypy

Gatewaypy es un pequeño gestor de tokens en Python diseñado para manejar accesos de aplicaciones y tokens de manera eficiente.

## Estructura de Carpetas

```
📦src
 ┣ 📂blueprints
 ┃ ┣ 📜app_routes.py
 ┃ ┣ 📜auth_routes.py
 ┃ ┗ 📜user_routes.py
 ┣ 📂config
 ┃ ┗ 📜config.json
 ┣ 📂database
 ┃ ┣ 📜estructurar.py
 ┃ ┣ 📜models.py
 ┃ ┗ 📜mydb.db
 ┣ 📂logs
 ┣ 📂managements
 ┃ ┣ 📜app_management.py
 ┃ ┣ 📜token_management.py
 ┃ ┗ 📜user_management.py
 ┣ 📂other
 ┣ 📂tests
 ┃ ┗ 📜test_cases.py
 ┣ 📜main.py
 ┗ 📜Resumen.md
```

- **config:** Contiene archivos de configuración, como `config.json`, que pueden incluir información de conexión a la base de datos, secretos para la generación de tokens, etc.
- **database:** Contiene archivos relacionados con la base de datos.
  - **models.py:** Define los modelos de la base de datos (tablas como Accesos, Aplicaciones, Tokens).
  - **db_utils.py:** Funciones útiles para interactuar con la base de datos (conexión, consultas, etc.).
- **auth:** Contiene la lógica de autenticación y manejo de tokens.
  - **auth_utils.py:** Funciones para autenticar usuarios y aplicaciones.
  - **token_management.py:** Manejo de la creación, validación y renovación de tokens.
- **api:** Se encarga de la lógica de la API del gateway.
  - **gateway_routes.py:** Define las rutas del gateway y la lógica asociada.
  - **api_utils.py:** Funciones auxiliares para el procesamiento de las solicitudes API.
- **tests:** Para almacenar pruebas unitarias y de integración.
  - **test_cases.py:** Pruebas para asegurarse de que cada parte del sistema funciona como se espera.
- **main.py:** El punto de entrada del programa. Aquí se configura e inicia el servidor Flask y se conecta con las demás partes del sistema.

## Documentación del Servidor

### Descripción General:

Gatewaypy es un servidor que gestiona el acceso a diferentes aplicaciones a través de tokens. Utiliza Flask como backend y JSON para la comunicación.

### Instrucciones de Ejecución:

Para ejecutar el servidor, asegúrate de tener todas las dependencias instaladas y luego simplemente ejecuta el archivo `main.py`.

### Configuración:

- El archivo `config.json` contiene los parámetros de configuración, como el host, puerto y rutas de archivos.
- Puedes modificar estos valores en el archivo de configuración según tus necesidades.
  {
  "Gateway": {
  "host": "0.0.0.0",
  "port": 5000,
  "debug": true
  },
  "Paths": {
  "logPath": "src/logs",
  "dbPath": "src/database/mydb.db"
  }
  }

### API:

- La API del servidor proporciona rutas para la gestión de tokens y acceso a las aplicaciones.
- Se admiten varios métodos HTTP, como GET, POST, etc.
- Consulta la documentación de la API para obtener detalles sobre las rutas disponibles y ejemplos de solicitudes y respuestas.

### Estructura del Proyecto:

La estructura de carpetas y archivos está diseñada para mantener una organización clara y modular del código.

### Manejo de Errores y Excepciones:

El servidor maneja cuidadosamente los errores y excepciones para garantizar un funcionamiento estable y confiable.

## Base Datos

Accesos: Para almacenar información sobre los usuarios autorizados a acceder al gateway.
Aplicaciones: Para almacenar información sobre las aplicaciones registradas en el gateway.
Tokens: Para almacenar información sobre los tokens generados para las aplicaciones.
A continuación, definiré el esquema de cada tabla y luego escribiré el script de migración para crearlas en la base de datos SQLite.

Esquema de la Base de Datos SQLite:
Accesos:

idUnico (INTEGER, PRIMARY KEY): Identificador único del acceso.
usuario (TEXT): Nombre de usuario habilitado para el acceso.
clave (TEXT): Contraseña del usuario.
App (TEXT): Nombre de la aplicación asociada al acceso.
habilitado (INTEGER): Indica si el acceso está habilitado (1) o deshabilitado (0).
Aplicaciones:

idUnicoApp (INTEGER, PRIMARY KEY): Identificador único de la aplicación.
nombreApp (TEXT): Nombre de la aplicación.
urlBackend (TEXT): URL del backend asociado a la aplicación.
infoAdicional (TEXT): Información adicional sobre la aplicación.
Tokens:

idUnico (INTEGER, PRIMARY KEY): Identificador único del token.
idUnicoApp (INTEGER): Identificador único de la aplicación asociada al token.
fechaCreacion (TEXT): Fecha de creación del token.
fechaExpiracion (TEXT): Fecha de expiración del token.
usuarioSolicitante (TEXT): Usuario que solicitó el token.

Insertar usuario:
{
"usuario": "nombre_de_usuario",
"clave": "contraseña",
"App": "nombre_de_la_aplicación",
"habilitado": 1 // 1 para habilitado, 0 para deshabilitado
}

Actualizar usuario:
{
"usuario": "nuevo_nombre_de_usuario",
"clave": "nueva_contraseña",
"App": "nuevo_nombre_de_la_aplicación",
"habilitado": 1 // 1 para habilitado, 0 para deshabilitado
}
