# Virtual environment


## Virtual environment- Using CMD

### Create virtual environment
`python -m venv dev_env`

###  Start/stop virtual environment
Start- `source dev_env/bin/activate`  
Stop- `deactivate`

## Virtual environment- Using PyCharm

### Create virtual environment
From IDE - https://www.youtube.com/watch?v=2P30W3TN4nI

###  Start/stop/check virtual environment
Start- `source venv/bin/activate`  
Stop- `deactivate`  
Check- `which python3`  
(Python location will be from venv) 

# Django project setup

### Install Django
`pip install django`

###  Create Django project
`django-admin startproject myproject`  
`cd myproject`

###  Create Django app
`python manage.py startapp myapp`

## How to run
### Install dependencies
`pip install -r requirements.txt`   

### Create project
- Create 2 directories backend, py_client
- `cd backend`
- `django-admin startproject cfehome .`
- Run `python manage.py runserver`

###  Notes
- Django project can have multiple Django apps
- Django project must have at least 1 app
- 
