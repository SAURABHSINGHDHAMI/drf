# DRF Setup

## Step 1: Create Virtual Environment and Activate It

```bash
py -m venv env
```
```bash
env\Scripts\activate
```

## Step 2: Install Django

```bash
pip install django
```

## Step 3: Create Django Project

```bash
django-admin startproject core
```

## Step 4: Install Django REST Framework

```bash
pip install djangorestframework
```

## Step 5: Configure Django to Use Django REST Framework

Add `rest_framework` to your `INSTALLED_APPS` setting in `core/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Django project is now set up with Django REST Framework!
