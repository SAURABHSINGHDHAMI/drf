from home.views import index, person, login, PersonAPI
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('person_api/', PersonAPI.as_view())
]