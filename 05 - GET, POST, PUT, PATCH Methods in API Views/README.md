# API View Methods and Usage

## Views Setup

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def index(request):

    courses = {
        'course_name': 'Python',
        'course_topics': ['Flask', 'Django', 'Tornado', 'FastAPI'],
        'course_provider': 'harvard'
    }

    if request.method == 'GET':
        print('YOU HIT A GET METHOD')
        return Response(courses)
    elif request.method == 'POST':
        print('YOU HIT A POST METHOD')
        return Response(courses)
    elif request.method == 'PUT':
        print('YOU HIT A PUT METHOD')
        return Response(courses)
    elif request.method == 'PATCH':
        print('YOU HIT A PATCH METHOD')
        return Response(courses)
```

## Handling POST Data

```python
if request.method == 'POST':
    data = request.data
    specific_value = data.get('name')  # Example to get a specific key from the POST data
```

## Using Query Parameters in GET Requests

```python
if request.method == 'GET':
    search_query = request.GET.get('search')
```

## Example Usage

### Sending a GET Request

To send a GET request with a query parameter, you can use the following URL:

```
http://127.0.0.1:8000/api/index/?search=saurabh
```

In the `index` view, you can handle this request and access the `search` parameter:

```python
if request.method == 'GET':
    search_query = request.GET.get('search')
```

### Sending a POST Request

To send data from the frontend to the backend using a POST request, you can send a JSON payload.

```python
if request.method == 'POST':
    data = request.data
    specific_value = data.get('name')
```
