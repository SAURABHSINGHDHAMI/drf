# ModelViewSet in Django Rest Framework

Django Rest Framework (DRF) provides the `ModelViewSet` class, which simplifies the process of creating CRUD APIs by encapsulating all the CRUD operations in a single class. This allows developers to focus more on the application logic rather than the boilerplate code for handling CRUD operations.

## Using ModelViewSet

The `ModelViewSet` class in DRF can handle all CRUD operations with minimal code.

### views.py

```python
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
```

In this example, the `PersonViewSet` class inherits from `ModelViewSet` and specifies the serializer class and the queryset. This setup automatically provides endpoints for listing, creating, retrieving, updating, and deleting `Person` instances.

### urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls))
]
```

In this setup, a `DefaultRouter` is used to automatically generate the URL patterns for the `PersonViewSet`. The `register` method of the router registers the viewset with a base URL of `person/`.

## Adding Custom Functionality

To add custom functionality, such as search, you can override the methods of the `ModelViewSet`.

### views.py with Search Functionality

```python
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)
        serializer = PersonSerializer(queryset, many=True)
        return Response({'status': 200, 'data': serializer.data})
```

In this modified example, the `list` method is overridden to add search functionality. The method filters the `Person` instances by their name if a `search` query parameter is provided.

## Summary

- **ModelViewSet**: Simplifies the creation of CRUD APIs by providing a single class that handles all CRUD operations.
- **Minimal Code**: Requires only a few lines of code to set up a fully functional CRUD API.
- **Automatic URL Routing**: Uses DRF routers to automatically generate URL patterns for the viewset.
- **Custom Functionality**: Methods of `ModelViewSet` can be overridden to add custom functionality such as search.
