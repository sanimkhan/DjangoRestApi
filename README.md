# Django REST API Learning Project
Welcome to my Django REST API learning project! 🚀

## Project Overview
This repository serves as my dedicated space for learning Django and exploring the intricacies of REST API development. The goal is to build a solid foundation in Django and progressively delve into the world of creating powerful and efficient RESTful APIs.

## Virtual environment

### Using CMD

#### Create virtual environment
`python -m venv dev_env`

####  Start/stop virtual environment
Start- `source dev_env/bin/activate`  
Stop- `deactivate`

### Using PyCharm

#### Create virtual environment
From IDE - https://www.youtube.com/watch?v=2P30W3TN4nI

####  Start/stop/check virtual environment
Start- `source venv/bin/activate`  
Stop- `deactivate`  
Check- `which python3`  
(Python location will be from venv) 

## Django project setup

### Install Django
`pip install django`

### Create project
- Create 2 directories backend, py_client  
`cd backend`
- Create project  
`django-admin startproject cfehome .`
- Run project  
`python manage.py runserver`
- Create app  
`python manage.py startapp api`

### Activate as django project
- Go to File -> Settings -> Languages & Frameworks -> Django and check the Enable Django Support box.
- Specify the Django project root, settings file, and manage script. These are usually located in the same folder as your project name.
- Click OK to save the settings and activate your Django project.

### Mark source folder project
- Mark the root folder of your project as a source root in PyCharm
- Right-click on the project folder
- Select Mark Directory as > Sources Root


## How to run
### Install dependencies
`pip install -r requirements.txt`

### Run
`python manage.py runserver`  
`python manage.py runserver 8000`

## Django commands

### Migrations
`python manage.py makemigrations`  
`python manage.py migrate`

### Shell
`python manage.py shell`
`cntrl+z`

### Create user
`python manage.py createsuperuser`

##  Notes
- Django project can have multiple Django apps
- Django project must have at least 1 app
- 


##  Tutorial
### JWT authentication
https://pythonguides.com/jwt-authentication-using-django-rest-framework/

