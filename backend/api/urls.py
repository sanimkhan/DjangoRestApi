from django.urls import path
from . import views

urlpatterns = [
    path('general-response', views.api_general_response),
    path('django-response', views.api_django_response_get),
]
