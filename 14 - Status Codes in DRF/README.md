# Status Codes in Django Rest Framework

Status codes are crucial for indicating the result of HTTP requests and are useful for frontend developers to understand the outcome of their API calls. Django Rest Framework (DRF) provides a set of standard status codes that can be used to indicate success, failure, or other outcomes of API requests.

## Using Status Codes

In DRF, you can use the `status` module to include appropriate status codes in your API responses.

### views.py

Here's how to use status codes in your `PersonViewSet` class:

```python
from rest_framework import viewsets, status
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
        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)
```

In this example, the `list` method uses `status.HTTP_200_OK` to indicate a successful retrieval of the data. The `status` module provides many other status codes, such as `HTTP_201_CREATED`, `HTTP_400_BAD_REQUEST`, and `HTTP_404_NOT_FOUND`, which you can use as needed.

## Summary

- **Status Codes**: Indicate the result of HTTP requests, useful for frontend developers to handle API responses.
- **DRF Status Module**: Provides a set of standard status codes for use in your API responses.

By properly using status codes, you can ensure that your API communicates effectively with frontend applications, making it clear whether an operation was successful, failed, or encountered some other condition.

## Full Example

### views.py with Status Codes

```python
from rest_framework import viewsets, status
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
        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

This example includes handling for `list`, `create`, `retrieve`, `update`, and `destroy` actions, each with appropriate status codes to indicate the outcome of the request.
