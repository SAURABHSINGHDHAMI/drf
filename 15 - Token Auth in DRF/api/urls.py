from home.views import index, person, login, PersonAPI, PersonViewSet, RegisterAPI, LoginAPI
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename = 'person')

urlpatterns = [
    path('index/', index),
    path('person_detail/', person),
    path('register_api/', RegisterAPI.as_view()),
    path('login_api/', LoginAPI.as_view() ),
    path('login/', login),
    path('person_api/', PersonAPI.as_view()),
    path('', include(router.urls))
]