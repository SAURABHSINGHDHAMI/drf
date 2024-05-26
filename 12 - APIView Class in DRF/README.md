# APIView Class in Django Rest Framework

The `APIView` class in Django Rest Framework (DRF) provides a way to handle different HTTP methods (GET, POST, PUT, PATCH, DELETE) in a class-based approach, offering better encapsulation and reduced code redundancy compared to using function-based views with the `api_view` decorator.

## APIView vs. api_view Decorator

- **api_view Decorator**: Adds HTTP methods to a function-based view.
- **APIView Class**: Encapsulates all CRUD methods (GET, POST, PUT, PATCH, DELETE) within a class, automatically routing to the appropriate method based on the HTTP request. This reduces code duplication and improves maintainability.

## Implementation

### views.py

Using the `APIView` class to handle different HTTP methods:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

class PersonAPI(APIView):
    
    def get(self, request):
        obj = Person.objects.all()
        serializer = PersonSerializer(obj, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})
```

In this example, the `PersonAPI` class handles all CRUD operations for the `Person` model. Each method corresponds to a specific HTTP request type and contains the logic for handling that request.

### urls.py

To route requests to the `PersonAPI` class, update the `urls.py` file:

```python
from django.urls import path
from home.views import PersonAPI

urlpatterns = [
    path('person_api/', PersonAPI.as_view())
]
```

This setup maps the URL path `person_api/` to the `PersonAPI` view, allowing DRF to route HTTP requests to the appropriate method in the `PersonAPI` class.

## Summary

- **Class-based Approach**: `APIView` provides a more organized and maintainable way to handle CRUD operations compared to function-based views with `api_view`.
- **Encapsulation**: All HTTP methods are encapsulated within a single class, reducing code duplication.
- **Automatic Routing**: DRF automatically routes the request to the correct method based on the HTTP request type.
