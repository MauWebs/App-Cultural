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

Login:

    http://127.0.0.1:8000/user/post/login/

Register:
    
    http://127.0.0.1:8000/user/post/register/

Register editor:

    http://127.0.0.1:8000/user/post/register/editor/

Register admin:

    http://127.0.0.1:8000/user/post/register/admin/

Actualizar usuarios:
    
    http://127.0.0.1:8000/user/put/

Perfil del usuario:
    
    http://127.0.0.1:8000/user/get/profile/

Mostrar un usuario en especial {ID}:
    
    http://127.0.0.1:8000/user/get/{id}/

Mostrar todos los usuarios:
    
    http://127.0.0.1:8000/user/get/all/

------------------------------------------------------

### Endpoints DigitalObject (Contenido):

Crear DigitalObject(Solo Administradores):

    http://127.0.0.1:8000/digitalObject/post/

Actualizar DigitalObject(Administradores o Editores):

    http://127.0.0.1:8000/digitalObject/put/{id}/

Ver todos los DigitalObjects:

    http://127.0.0.1:8000/digitalObject/get/all/

digitalObject por {ID}:

    http://127.0.0.1:8000/digitalObject/getId/{id}/

> [!WARNING]
> Está en mantenimiento, funcionalidad inestable

Darle un puntaje a un digitalObject (EN PROCESO...):

    http://127.0.0.1:8000/digitalObject/postRating/

> [!WARNING]
> Está en mantenimiento, funcionalidad inestable

Crear un comentario a un digitalObject (EN PROCESO...):
    
    http://127.0.0.1:8000/digitalObject/getId/{id}/comment/

------------------------------------------------------

#### Desarrollador:

[💻 Mau_Webs](https://github.com/MauWebs?tab=repositories)