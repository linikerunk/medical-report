# Challenged Mapes Solutions
![MAPES](https://user-images.githubusercontent.com/27506588/94381799-e64f6700-0110-11eb-9dc1-ef803d3e146e.png)


This is a challenge for the MAPESolutions where needs to do a sequence of steps, the step that need to implementation is below.

The test consists of implementing a scenario, to demonstrate knowledge in the following
technologies: django, jquery, bootstrap, postgresql and unit tests.
 - Django
 - jQuery
 - Bootstrap
 - Postgresql
 - Unit tests
 - Deploy on Heroku

# Modelo de Template
![Captura de tela de 2020-09-27 23-15-46](https://user-images.githubusercontent.com/27506588/94383969-e2731300-0117-11eb-8f1a-3ad0265de30c.png)



# How to run this project
```sh
# python version 3.8 
git remote add origin https://github.com/linikerunk/medical-report.git

python -m venv venv_name /
python3 -m venv venv_name 

pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Test
  - Lib - Coverage
  - Django - django.test

```sh
coverage manage.py run
coverage report
coverage html
```
this is a test doing for the data migrate  for two files [consulta.csv] [exames.csv]
![test](https://user-images.githubusercontent.com/27506588/94382283-80fc7580-0112-11eb-9511-9d1e3bcd1195.png)

![first _test](https://user-images.githubusercontent.com/27506588/94382157-13504980-0112-11eb-8a77-9893a87873ed.png) 

# Insert date in the tables 
![datamigrate](https://user-images.githubusercontent.com/27506588/94382467-2d3e5c00-0113-11eb-8005-2cfe0108e1f3.png)


# PostegreSQL
![post](https://user-images.githubusercontent.com/27506588/94382531-6bd41680-0113-11eb-9305-27674c5ea915.png)
