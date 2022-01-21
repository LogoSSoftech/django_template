# django_template
## DRF Template

This repository works as a base project to easily start an API with Django REST

You can use it locally, or with docker, or deploy it directly to your project on Heroku

### How to Use

- Create your own copy of the repository clicking on `Use this template button`, name it and clicking on `Create repository from template`

- Since you have created your own project, clone it and enter your project file

- Run your project with your preferred method

### There are 3 methods to use your new project

**NOTE:**
You can use `openssl rand -base64 32` command in you terminal to generate a django secret key

## Run your project locally

- Uncomment the `DEBUG = False` constant

- Uncomment too the `DATABASES` dict below `### FOR RUN LOCALLY ####` section and set  the values with the respective data

- Execute following commands:

```python manage.py makemigrations```
```python manage.py migrate```
```python manage.py runserver 0.0.0.0:8000```

## Run your project using Docker

- In your main folder, create a copy of the `.env.example` file and use it as a guide to fill it with the respective information

```cp .env.example .env```


- Open your `settings.py` and uncomment the `# DEBUG = os.getenv('DEBUG')` line

- Uncomment too the `DATABASES` dict below `#### FOR RUN WITH DOCKER ####` section

- Execute the docker compose command to build project and run your project

```sudo docker-compose up -d --build```
