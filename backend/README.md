# E-commercesource

## I. Setup backend env in Linux
### 1. Navigate to backend sourcecode

``cd backend``

### 2. Create a virtual env

``python3.9 -m venv .venv``

### 3. Activate virtual env

``source .venv/bin/active``

### 4. Setup the virtual env

``pip install -r requirements.txt``

### 5. Add pre-commit hook

``pre-commit install``

### 6. Migrate database

``python manage.py migrate``

### 7. Create master data

``python manage.py init_master_data``

### 8. Create super staff

```python manage.py createsuperuser```

### 9. Run app

``python manage.py runserver``
