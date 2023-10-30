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
-tzdata==2023.3

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

### Endpoints Users:

Login:

    http://127.0.0.1:8000/users/login/

Register:
    
    http://127.0.0.1:8000/users/register/

Actualizar user:
    
    http://127.0.0.1:8000/users/put/

Perfil del usuario:
    
    http://127.0.0.1:8000/users/userProfile/

Mostrar un usuario en especial {ID}:
    
    http://127.0.0.1:8000/users/{id}/

Mostrar todos los users:
    
    http://127.0.0.1:8000/users/getUsers/

------------------------------------------------------

### Endpoints DigitalObjects (Contenido):

Crear DigitalObject:

    http://127.0.0.1:8000/digitalObjects/post/

Ver todos los DigitalObjects:

    http://127.0.0.1:8000/digitalObjects/getAll/

digitalObjects

    http://127.0.0.1:8000/digitalObjects/getId/{id}/

> [!WARNING]
> Está en mantenimiento, funcionalidad inestable

Darle un puntaje a un digitalObjects (EN PROCESO...):

    http://127.0.0.1:8000/digitalObjects/postRating/

> [!WARNING]
> Está en mantenimiento, funcionalidad inestable

Crear un comentario a un digitalObject (EN PROCESO...):
    
    http://127.0.0.1:8000/digitalObjects/getId/{id}/comment/

------------------------------------------------------

#### Desarrollador:

[💻 Mau_Webs](https://github.com/MauWebs?tab=repositories)