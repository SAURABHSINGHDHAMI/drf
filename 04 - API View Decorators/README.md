# API View Decorators in Django REST Framework

## Setup

### 1. Create a Django App

```bash
python manage.py startapp home
```

### 2. Install the App in `settings.py`

Add `'home'` to the `INSTALLED_APPS` list.

```python
INSTALLED_APPS = [
    ...
    'home',
]
```

## API Views

### Django vs DRF Views

- **Django Views**: Deals with rendering templates.
- **DRF (Django REST Framework) Views**: Deals with JSON.

### API View Decorator

- `@api_view`: A decorator that converts an existing Django/Python function into an API view function.
  - **GET** method: Retrieve data.
  - **POST** method: Create data.
  - **PUT & PATCH** methods: Update data.
  - **DELETE** method: Delete data.

## Implementation

### 1. Define API View in `views.py`

Create the `index` view in `home/views.py`:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    courses = {
        'course_name': 'Python',
        'course_topics': ['Flask', 'Django', 'Tornado', 'FastAPI'],
        'course_provider': 'Harvard'
    }
    return Response(courses)
```

### 2. Create Separate API Directory for Handling APIs

Create an `api` directory and add `__init__.py` and `urls.py`:

```
api
├── __init__.py
└── urls.py
```

### 3. Define URL Patterns in `api/urls.py`

```python
from home.views import index
from django.urls import path

urlpatterns = [
    path('index/', index),
]
```

### 4. Set Project Routes in Main `urls.py`

Update the main `urls.py` to include the API routes:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

## Migrations and Running the Server

### 1. Apply Migrations

```bash
python manage.py migrate
```

### 2. Run the Server

```bash
python manage.py runserver
```

## Testing APIs

Use Postman or a similar tool to test the APIs.

- **GET Request**: Send a GET request to `http://127.0.0.1:8000/api/index/`.

You should receive a JSON response similar to:

```json
{
    "course_name": "Python",
    "course_topics": ["Flask", "Django", "Tornado", "FastAPI"],
    "course_provider": "Harvard"
}
```
