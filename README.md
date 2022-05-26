# Docker with REST Framework

## commands to start the project

```zsh
mkdir docker
cd docker
touch Dockerfile
docker build . -t python:tahani
docker images
code docker-compose.yml
docker-compose up
poetry init -n
poetry shell
poetry add django && poetry add --dev black flake8
django-admin startproject blog_api_project .
docker python manage.py migrate
python manage.py startapp posts
python manage.py createsuperuser --email=tahany@ltuc.com --username=admin
poetry add djangorestframework
### create your model
python manage.py makemigrations
python manage.py migrate

poetry export -f requirements.txt -o requirements.txt --without-hashes

docker-compose up --build
docker-compose up -d
##or
docker rm docker_web_1
docker rmi docker_web


## finally
docker container stop $(docker container ls -a -q); docker system prune -a -f --volumes
docker-compose down
```
### INSTALLED_APPS in settings.py
```python
     #Third party
     'rest_framework',
     #local apps
     'posts',
```


### admin.py

```python
     from django.contrib import admin
     from .models import Posts
     # Register your models here.

     admin.site.register(Posts)
```
### settings.py

* not secure way 
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
           'rest_framework.permissions.AllowAny',
         ]
     }
    ```
### urls.py for project

```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
          path('admin/', admin.site.urls),
          path('api/v1/posts/', include('posts.urls')),
     ]
```
### urls.py for app

```python
     from django.urls import path
     from .views import PostList, PostDetail

     urlpatterns = [
        path('', PostList.as_view(), name='post_list'),
        path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
     ]
```

## **Serializers – Django REST Framework**

> Serializers in Django REST Framework are responsible for converting objects into data types understandable by javascript and front-end frameworks.

> Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

### serializers.py

```python 
from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at', 'updated_at')
        model = Posts
```

### views.py

```python
from rest_framework import generics
from .serializers import PostSerializer
from .models import Posts
# Create your views here.

class PostList(generics.ListAPIView):
    """
    List all posts
    """
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    """
    List a single post
    """
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
```

### important commands

```bash
##first commands =>

docker-compose up --build 

docker-compose up -d

##or
docker-compose up -d --build

##a command to convert pyproject.toml dependencies to requirements.txt

poetry export -f requirements.txt -o requirements.txt


##to load the dependencies that in the requirements.txt  file

pip install -r requirements.txt

###################
docker-compose run web python manage.py migrate

docker container stop $(docker container ls -a -q); docker system prune -a -f --volumes

docker-compose down

```


* To change Remote origin repo on (Github)

```bash
git remote -v
git remote set-url origin NEW_URL
```

### Error

``ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?``

### solve:

``poetry export -f requirements.txt -o requirements.txt --without-hashes``

### PORT 

``http://127.0.0.1:8001/api/v1/posts/``