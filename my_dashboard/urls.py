from django.urls import path, include
from . import views
from .views import suggestions_view

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/suggestions/', suggestions_view, name='suggestions'),
]