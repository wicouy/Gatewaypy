## Índice

1. [Cargar configuración](#cargar-configuración)
2. [Listar todos los usuarios](#listar-todos-los-usuarios)
3. [Insertar un nuevo usuario](#insertar-un-nuevo-usuario)
4. [Eliminar un usuario existente](#eliminar-un-usuario-existente)
5. [Actualizar un usuario existente](#actualizar-un-usuario-existente)
6. [Validar credenciales de usuario](#validar-credenciales-de-usuario)

### Cargar configuración

- Método: POST
- URL: `http://localhost:5000/config/load`
- Cuerpo de la solicitud (formato JSON):
  ```json
  {
    "config_path": "/ruta/al/archivo/configuracion.json"
  }
  ```
- Acción:
  - Abre Postman.
  - Selecciona el método POST.
  - Ingresa la URL proporcionada.
  - Selecciona la pestaña "Cuerpo".
  - Selecciona "JSON" como tipo de contenido.
  - Ingresa la ruta al archivo de configuración en el formato JSON proporcionado.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - El contenido del archivo de configuración cargado correctamente.

### Listar todos los usuarios

- Método: GET
- URL: `http://localhost:5000/users`
- Acción:
  - Abre Postman.
  - Selecciona el método GET.
  - Ingresa la URL proporcionada.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Todos los usuarios almacenados en la base de datos, devueltos como una lista JSON.

### Insertar un nuevo usuario

- Método: POST
- URL: `http://localhost:5000/api/users`
- Cuerpo de la solicitud (formato JSON):
  ```json
  {
    "usuario": "nombre_de_usuario",
    "clave": "contraseña",
    "App": "nombre_de_la_aplicación",
    "habilitado": true
  }
  ```
- Acción:
  - Abre Postman.
  - Selecciona el método POST.
  - Ingresa la URL proporcionada.
  - Selecciona la pestaña "Cuerpo".
  - Selecciona "JSON" como tipo de contenido.
  - Ingresa los datos del nuevo usuario en el formato JSON proporcionado.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que el usuario se insertó con éxito.

### Eliminar un usuario existente

- Método: DELETE
- URL: `http://localhost:5000/api/users/<user_id>`
- Acción:
  - Abre Postman.
  - Selecciona el método DELETE.
  - Ingresa la URL proporcionada, reemplazando `<user_id>` con el ID del usuario que deseas eliminar.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que el usuario se eliminó con éxito.

### Actualizar un usuario existente

- Método: PUT
- URL: `http://localhost:5000/api/users/<user_id>`
- Cuerpo de la solicitud (formato JSON):
  ```json
  {
    "usuario": "nuevo_nombre_de_usuario",
    "clave": "nueva_contraseña",
    "App": "nuevo_nombre_de_la_aplicación",
    "habilitado": false
  }
  ```
- Acción:
  - Abre Postman.
  - Selecciona el método PUT.
  - Ingresa la URL proporcionada, reemplazando `<user_id>` con el ID del usuario que deseas actualizar.
  - Selecciona la pestaña "Cuerpo".
  - Selecciona "JSON" como tipo de contenido.
  - Ingresa los nuevos valores del usuario en el formato JSON proporcionado.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que el usuario se actualizó con éxito.

### Validar credenciales de usuario

- Método: POST
- URL: `http://localhost:5000/auth/validate`
- Cuerpo de la solicitud (formato JSON):
  ```json
  {
    "username": "nombre_de_usuario",
    "password": "contraseña"
  }
  ```
- Acción:
  - Abre Postman.
  - Selecciona el método POST.
  - Ingresa la URL proporcionada.
  - Selecciona la pestaña "Cuerpo".
  - Selecciona "JSON" como tipo de contenido.
  - Ingresa el nombre de usuario y la contraseña en el formato JSON proporcionado.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando si las credenciales son válidas o no.
