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

    http://127.0.0.1:8000/digitalObject/getId/{id}/

------------------------------------------------------

### Endpoints Comentario (Comment):

```js
{
    "description":"description"
}
```
Crear un comentario a un digitalObject:

    http://127.0.0.1:8000/digitalObject/getId/{id}/comment/

------------------------------------------------------

### Endpoints Rating (Estrellas):

> [!WARNING]
> Está en mantenimiento (INESTABLE)

```js
{
    "rating_value":5
}
```

Darle un puntaje a un digitalObject:

    http://127.0.0.1:8000/digitalObject/postRating/

------------------------------------------------------

### Endpoints Suggestions (Sugerencias):

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

Crear una realidad virtual 3d (Administradores):

    http://127.0.0.1:8000/virtualReality/post/

------------------------------------------------------

#### Desarrollador:

[💻 Mau_Webs](https://github.com/MauWebs?tab=repositories)
