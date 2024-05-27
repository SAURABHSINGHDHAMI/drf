# Django Rest Framework (DRF) Token Authentication

Token authentication is a mechanism that allows users to authenticate using tokens instead of traditional methods like username/password or sessions.

## Setup

### Install and Configure DRF Token Authentication

1. Add the required authentication classes in your `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

2. Add `rest_framework.authtoken` to your `INSTALLED_APPS` and run migrations:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]
```

Run the migration command:
```sh
python manage.py migrate
```

## Creating Serializers

### RegisterSerializer

Define a serializer to handle user registration:

```python
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('Username is taken')
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Email is taken')
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
```

### LoginSerializer

Define a serializer for user login:

```python
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
```

## Creating Views

### RegisterAPI

Create a view to handle user registration:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({'status': True, 'message': 'User created'}, status=status.HTTP_201_CREATED)
```

### LoginAPI

Create a view to handle user login and token generation:

```python
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'status': True, 'message': 'User login', 'token': str(token)}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': False, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
```

## Updating URLs

Add the API views to your `urls.py`:

```python
from django.urls import path
from home.views import RegisterAPI, LoginAPI

urlpatterns = [
    path('register_api/', RegisterAPI.as_view()),
    path('login_api/', LoginAPI.as_view()),
]
```

## Using Token Authentication

To restrict access to authenticated users only, you can use DRF's permissions.

### Summary

- **Token Authentication**: Use tokens for user authentication, simplifying the process of securing your API.
- **User Registration and Login**: Create API endpoints for user registration and login, generating tokens for authenticated users.
- **Permissions**: Restrict access to your API endpoints using DRF's built-in permission classes.
