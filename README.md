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