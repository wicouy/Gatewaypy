## Índice

1. [Obtener todos los endpoints](#obtener-todos-los-endpoints)
2. [Crear un nuevo endpoint](#crear-un-nuevo-endpoint)
3. [Eliminar un endpoint existente](#eliminar-un-endpoint-existente)
4. [Actualizar un endpoint existente](#actualizar-un-endpoint-existente)

### Obtener todos los endpoints

- Método: GET
- URL: `http://localhost:5000/endpoints`
- Acción:
  - Abre Postman.
  - Selecciona el método GET.
  - Ingresa la URL proporcionada.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Todos los endpoints almacenados en la base de datos, devueltos como una lista JSON.

### Crear un nuevo endpoint:

- Método: POST
- URL: `http://localhost:5000/api/endpoints`
- Cuerpo de la solicitud (formato JSON):
  ```json
  {
    "nombre_endpoint": "nombre_del_endpoint",
    "metodo_http": "GET",
    "tipo_respuesta": "JSON",
    "requiere_token": true,
    "url_backend": "http://backend.example.com",
    "puerto_backend": 8080,
    "info_adicional": "Información adicional del endpoint",
    "habilitado": true
  }
  ```
- Acción:
  - Abre Postman.
  - Selecciona el método POST.
  - Ingresa la URL proporcionada.
  - Selecciona la pestaña "Cuerpo".
  - Selecciona "JSON" como tipo de contenido.
  - Ingresa los datos del nuevo endpoint en el formato JSON proporcionado.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que el endpoint se creó con éxito.

### Eliminar un endpoint existente:

- Método: DELETE
- URL: `http://localhost:5000/api/endpoints/<endpoint_id>`
- Acción:
  - Abre Postman.
  - Selecciona el método DELETE.
  - Ingresa la URL proporcionada, reemplazando `<endpoint_id>` con el ID del endpoint que deseas eliminar.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que el endpoint se eliminó con éxito.

### Actualizar un endpoint existente:

- Método: PUT
- URL: `http://localhost:5000/api/endpoints/<endpoint_id>`
- Cuerpo de la solicitud (formato JSON):
  ```json
  {
    "nombre_endpoint": "nuevo_nombre_del_endpoint",
    "metodo_http": "PUT",
    "tipo_respuesta": "XML",
    "requiere_token": false,
    "url_backend": "http://new-backend.example.com",
    "puerto_backend": 9090,
    "info_adicional": "Nueva información adicional del endpoint",
    "habilitado": false
  }
  ```
- Acción:
  - Abre Postman.
  - Selecciona el método PUT.
  - Ingresa la URL proporcionada, reemplazando `<endpoint_id>` con el ID del endpoint que deseas actualizar.
  - Selecciona la pestaña "Cuerpo".
  - Selecciona "JSON" como tipo de contenido.
  - Ingresa los nuevos valores del endpoint en el formato JSON proporcionado.
  - Haz clic en el botón "Enviar" para realizar la solicitud.
- Respuesta esperada:
  - Un mensaje indicando que el endpoint se actualizó con éxito.
