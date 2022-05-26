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