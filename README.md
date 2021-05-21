# Wiztute Project
Wiztute backend server

## Wiztute Backend Server

## Contributors
* Akash Chandra

## Django-admin superuser

| Key | Value |
|----------|------------|
| Email | vishnu@wiztute.com | 
| Password| demo1234 |

## Prerequisite

| Packages | Version |
|----------|------------|
| virtualenv | 16.0.0 | 
| virtualenv-clone | 0.5.3 | 
| virtualenvwrapper| 4.8.4 |

## Setup
* virtualenv venv -p python3

* source ./venv/bin/activate
	
* pip3 install -r requirements.txt

* python3 manage.py makemigrations --settings=wiztute.settings

* python3 manage.py migrate --settings=wiztute.settings

* python3 manage.py runserver --settings=wiztute.settings 8080

* python3 manage.py runserver --settings=wiztute.settings 8080 --insecure

* python3 manage.py runserver --settings=wiztute.settings 0.0.0.0:8080  --> when on server

* python3 manage.py runserver --settings=wiztute.settings 0.0.0.0:8080 --insecure

* python3 manage.py runsslserver --certificate /etc/letsencrypt/live/wiztech.co.in/fullchain.pem --key /etc/letsencrypt/live/wiztech.co.in/privkey.pem --settings=wiztute.settings 0.0.0.0:8080

* chmod +x start.sh








