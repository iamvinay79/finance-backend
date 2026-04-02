# Finance Backend API

## Features

* JWT Authentication
* Role-based Access Control (Viewer, Analyst, Admin)
* Financial Records CRUD
* Dashboard Summary APIs
* Error Handling

## Tech Stack

* Django
* Django REST Framework
* SQLite


## Setup

git clone <repo-url>
cd finance-backend

python -m venv financeenv
source financeenv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


## APIs

* POST /api/token/
* GET /api/finance/records/
* POST /api/finance/records/
* GET /api/finance/dashboard/

## Author

Vinay Kumar
