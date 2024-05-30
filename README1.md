# Django - Understanding models

This is my project helps in understanding models and creating a database for our projects

## Table of contents

- [Overview](#overview)
  - [What are models](#What-is-Django)
  - [Requirements](#requirement)
- [My process](#my-process)
  - [Challenges](#challenges)

## Overview

In this project you will understand models and database system in django

### What-are-models

In django when the user types in his or her URL sreaches through your VEIWS and models(database) for informations
related to your sreach and then displays it on with templates .
Models helps us interact with the database to get information, they are also python class, Each model repersent a database table and each attribute is a field

### Requirements

1. Install the latest version of python
2. Install django
3. You must have the basic understanding of python

### Links

- Django Doc: [https://www.djangoproject.com/]

## My process

1. To start a django project you first need a virtal enviroment which helps in storing our dependencies we need for our project

```
  python -m venv env
```

2. Activate virtual environment

```
   env\Scripts\activate
```

3. Install Django

```
  pip install django
```

4. Start project by using this command

```
   django-admin startproject (projectname)
```

5. Start server by typing

```
  python manage.py runserver
```

6. Django consist of projects and multiple apps, create your app

```
   python manage.py startapp jobBoard
```

7. In your project folder there's file called setting.py,
   open it and navigate Installed_apps and add the name of your app (jobBoard)

8. In your jobBoard folder create a file called url.py
9. In your new file urls.py

   ```
    from django.urls import path
    urlpatterns = [
    path('', index),
    ]
   ```

10. In your project folder => urls.py => import include

```

    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('jobBoard.urls')),
    ]

```

11. In your views.py create a function called index

    ```
    from django.shortcuts import render, HttpResponse

    # Create your views here.
    def index(request):
        return HttpResponse("<h1>Job Board</h1>")
    ```

12. runserver

```
  python manage.py runserver
```

13. In your app folder open models.py =>
    in this file we're going to create a job posting table , that consist of title,description,company salary

    ```
      from django.db import models

      # Create your models here.

      class jobPosting(models.Model):
          # this section contains the feild on the table
          tittle = models.CharField(max_length=100)
          # textFeild are used for longer strings
          description = models.TextField()
          company = models.CharField(max_length=100)
          salary = models.IntegerField()
    ```

14. makemigration => creates instructions telling django how the db have changed.
    ```
    python manage.py makemigrations
    ```
15. migrate => Applies the above changes, it affects the db
    ```
    python manage.py migrate
    ```
