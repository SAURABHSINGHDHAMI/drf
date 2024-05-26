# Serializing Foreign Keys in DRF

When dealing with foreign key relationships in Django Rest Framework (DRF), you have several options for serializing related objects.

## models.py

```python
from django.db import models

class Color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name

class Person(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='color')
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
```

## serializers.py

```python
from rest_framework import serializers
from .models import Person, Color

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name']

class PersonSerializer(serializers.ModelSerializer):

    color = ColorSerializer()  # Serializing with another serializer class

    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1
```

In this example, `PersonSerializer` includes a `ColorSerializer` to serialize the related color object. This approach allows for more control over how the related object is serialized.

Alternatively, you can use the `depth` option in the `Meta` class of the serializer to automatically serialize related objects to a certain depth. For example:

```python
class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
        depth = 1
```

The `depth` option serializes all related objects up to the specified depth. However, using `depth` may include more data than necessary in the response, which could impact performance.

## views.py

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

@api_view(['GET'])
def person(request):

    if request.method == 'GET':
        obj = Person.objects.filter(color__isnull=True)
        serializer = PersonSerializer(obj, many=True)
        return Response(serializer.data)
```

In this example, we have an API endpoint that retrieves persons whose color is not specified (color__isnull=True). The PersonSerializer is used to serialize these objects.
