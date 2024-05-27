from home.views import index, person, login, PersonAPI, PersonViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename = 'person')

urlpatterns = [
    path('index/', index),
    path('person_detail/', person),
    path('login/', login),
    path('person_api/', PersonAPI.as_view()),
    path('', include(router.urls))
]