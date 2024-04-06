## Índice

1. [Listar todas las aplicaciones](#listar-todas-las-aplicaciones)
2. [Insertar una nueva aplicación](#insertar-una-nueva-aplicación)
3. [Eliminar una aplicación existente](#eliminar-una-aplicación-existente)
4. [Actualizar una aplicación existente](#actualizar-una-aplicación-existente)

### Listar todas las aplicaciones

- Método: GET
- URL: `http://localhost:5000/apps`
- Acción:
  - Abre Postman.
  - Selecciona el método GET.
  - Ingresa la URL proporcionada.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Todas las aplicaciones almacenadas en la base de datos, devueltas como una lista JSON.

### Insertar una nueva aplicación

- Método: POST
- URL: `http://localhost:5000/api/apps`
- Cuerpo de la solicitud (formato JSON):
  ```json
  {
    "nombre_app": "nombre_de_la_aplicación",
    "url_backend": "http://backend.example.com",
    "info_adicional": "Información adicional de la aplicación",
    "habilitado": true
  }
  ```
- Acción:
  - Abre Postman.
  - Selecciona el método POST.
  - Ingresa la URL proporcionada.
  - Selecciona la pestaña "Cuerpo".
  - Selecciona "JSON" como tipo de contenido.
  - Ingresa los datos de la nueva aplicación en el formato JSON proporcionado.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que la aplicación se insertó con éxito.

### Eliminar una aplicación existente

- Método: DELETE
- URL: `http://localhost:5000/api/apps/<app_id>`
- Acción:
  - Abre Postman.
  - Selecciona el método DELETE.
  - Ingresa la URL proporcionada, reemplazando `<app_id>` con el ID de la aplicación que deseas eliminar.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que la aplicación se eliminó con éxito.

### Actualizar una aplicación existente

- Método: PUT
- URL: `http://localhost:5000/api/apps/<app_id>`
- Cuerpo de la solicitud (formato JSON):
  ```json
  {
    "nombre_app": "nuevo_nombre_de_la_aplicación",
    "url_backend": "http://nuevo-backend.example.com",
    "info_adicional": "Nueva información adicional de la aplicación",
    "habilitado": false
  }
  ```
- Acción:
  - Abre Postman.
  - Selecciona el método PUT.
  - Ingresa la URL proporcionada, reemplazando `<app_id>` con el ID de la aplicación que deseas actualizar.
  - Selecciona la pestaña "Cuerpo".
  - Selecciona "JSON" como tipo de contenido.
  - Ingresa los nuevos valores de la aplicación en el formato JSON proporcionado.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que la aplicación se actualizó con éxito.
