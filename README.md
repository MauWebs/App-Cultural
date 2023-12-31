------------------------------------------------------

# Install App:

### Tecnologías utilizadas:

- Python (3.12.0)

- Django Rest Framework (3.14.0)

------------------------------------------------------

### Crear el entorno virtual:

```bash
pip install virtualenv
```

```bash
virtualenv env
```

------------------------------------------------------

### Activar el entorno virtual:

```bash
cd env/
```

```bash
cd Scripts/
```

```bash
activate
```

> [!IMPORTANT]
> Vuelve a tu carpeta original ejecutando

```bash
cd ../../
```

------------------------------------------------------

### Instalar dependencias:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> Esto te permite instalar las librerías

------------------------------------------------------

### Dependencias usadas:

- asgiref==3.7.2
- Django==4.2.6
- django-cors-headers==4.3.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.3.0
- PyJWT==2.8.0
- pytz==2023.3.post1
- setuptools==68.2.2
- sqlparse==0.4.4
- tzdata==2023.3

------------------------------------------------------

### Activar la App:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate  
```

```bash
python manage.py runserver
```

------------------------------------------------------

### Endpoints User:

```js
{
    "user_name":"name",
    "last_name":"lastname",
    "email":"user@gmail.com",
    "password":"123456"
}
```

Login:

    http://127.0.0.1:8000/user/post/login/

Register:
    
    http://127.0.0.1:8000/user/post/register/

Register editor:

    http://127.0.0.1:8000/user/post/register/editor/

Register admin:

    http://127.0.0.1:8000/user/post/register/admin/

Editar usuarios:
    
    http://127.0.0.1:8000/user/put/

Perfil del usuario:
    
    http://127.0.0.1:8000/user/get/profile/

Mostrar un usuario en especial {ID}:
    
    http://127.0.0.1:8000/user/get/{id}/

Mostrar todos los usuarios:
    
    http://127.0.0.1:8000/user/get/all/

------------------------------------------------------

### Endpoints DigitalObject (Contenido):

```js
{
    "title":"title",
    "description":"description",
    "place":"place",
    "format":"format",
    "tag":"tag",
    "url":"url"
}
```

Crear DigitalObject (Administradores):

    http://127.0.0.1:8000/digitalObject/post/

Editar DigitalObject (Administradores o Editores):

    http://127.0.0.1:8000/digitalObject/put/{id}/

Mostrar todos los DigitalObjects:

    http://127.0.0.1:8000/digitalObject/get/all/

Mostrar digitalObject por {ID}:

    http://127.0.0.1:8000/digitalObject/get/{id}/

Eliminar un digitalObject {ID}:

    http://127.0.0.1:8000/digitalObject/delete/{id}/

------------------------------------------------------

### Endpoints Comentario (Comment):

```js
{
    "description":"description"
}
```
Crear un comentario a un digitalObject {ID}:

    http://127.0.0.1:8000/digitalObject/post/{id}/comment/

Eliminar un comentario a un digitalObject {ID}:

    http://127.0.0.1:8000/digitalObject/delete/comment/{id}/

------------------------------------------------------

### Endpoints Rating (Estrellas):

> [!WARNING]
> Está en mantenimiento (INESTABLE)

```js
{
    "rating_value":5
}
```

Darle un puntaje a un digitalObject {ID}:

    http://127.0.0.1:8000/digitalObject/post/rating/{id}/

------------------------------------------------------

### Endpoints Suggestions (Sugerencias):

```js
{
    "description":"description"
}
```

Crear Suggestion (Administradores):

    http://127.0.0.1:8000/suggestion/post/

Editar Suggestion {ID} (Administradores):

    http://127.0.0.1:8000/suggestion/put/{id}/

Mostar todas las Suggestions:

    http://127.0.0.1:8000/suggestion/get/all/

Mostar Suggestion por {ID}:

    http://127.0.0.1:8000/suggestion/get/{id}/

------------------------------------------------------

### Endpoints Contacts (Contactanos):

```js
{
    "name":"name",
    "lastname":"lastname",
    "email":"email",
    "web":"web",
    "matter":"matter",
    "consultation":"consultation",
    "message":"message"
}
```

Crear un mensaje de contacto:

    http://127.0.0.1:8000/contacts/post/

Mostrar todos los mensajes de contacto:

    http://127.0.0.1:8000/get/all/

Mostrar contacto por {ID}:

    http://127.0.0.1:8000/get/{id}/
    
Eliminar contacto por {ID}:

    http://127.0.0.1:8000/delete/{id}/

------------------------------------------------------

### Endpoints New (Noticia):

```js
{
    "title":"title",
    "url":"url",
    "description":"description"
}
```

Crear una Noticia (Administradores):

    http://127.0.0.1:8000/news/post/

Editar una Noticia (Administradores o Editores):

    http://127.0.0.1:8000/news/put/{id}/

Eliminar una Noticia (Administradores):

    http://127.0.0.1:8000/delete/{id}/

Mostrar Noticias:

    http://127.0.0.1:8000/news/get/all/

Mostrar una Noticia por {ID}:

    http://127.0.0.1:8000/news/get/{id}/

------------------------------------------------------

### Endpoints VirtualReality (Realidad Virtual):

```js
{
    "title":"title",
    "description":"description",
    "place":"place",
    "format":"format",
    "tag":"tag",
    "img":"img"
}
```

Crear una realidad virtual 3D (Administradores):

    http://127.0.0.1:8000/virtualReality/post/

Eliminar realidad virtual 3D {ID} (Administradores):

    http://127.0.0.1:8000/virtualReality/delete/{id}/

Mostrar todos realidad virtual 3D:

    http://127.0.0.1:8000/virtualReality/get/all/

Mostrar realidad virtual 3D por {ID}:

    http://127.0.0.1:8000/virtualReality/get/{id}/

Crear o Actualizar imagen 3D por {ID}:

    http://127.0.0.1:8000/virtualReality/upload-image/{id}/

------------------------------------------------------

### Endpoints Historis (Historias):

```js
{
    "title":"titile",
    "description":"description",
    "format":"format",
    "tag":"tag",
    "url":"url"
}
```

Crear histories:

    http://127.0.0.1:8000/histories/post/
    
Eliminar histories:
    
    http://127.0.0.1:8000/histories/post/delete/<int:pk>/
    
Mostrar todos las histories:

    http://127.0.0.1:8000/histories/post/get/all/

------------------------------------------------------

### Endpoints Products (Productos):

```js
{
    "title":"titile",
    "description":"description",
    "price":"price",
    "url":"url"
}
```

Crear Products:

    http://127.0.0.1:8000/products/post/

Mostrar todos las Products:

    http://127.0.0.1:8000/products/get/all/

Eliminar Products {id}:

    http://127.0.0.1:8000/products/delete/{id}/

------------------------------------------------------

### Endpoints Sales (Ventas):

```js
{
    "products": ["product", "product", "product"],
    "total_amount": "total_amount",
}
```

Crear Products:

    http://127.0.0.1:8000/sales/post/


Mostrar todos las histories:

    http://127.0.0.1:8000/sales/get/all/

------------------------------------------------------

### Endpoints backup (Respaldo):

Crear un backup:

    http://127.0.0.1:8000/private/post/backup/

------------------------------------------------------

#### Desarrollador:

[💻 Mau_Webs](https://github.com/MauWebs?tab=repositories)