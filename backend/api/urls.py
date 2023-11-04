from django.urls import path
from .views import api_general_response, api_django_response_get

urlpatterns = [
    path('general-response', api_general_response),
    path('django-response', api_django_response_get),
]
