from django.urls import path, include
from . import views
from .views import suggestions_view,setMonitor

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('get-stock-data/', views.get_stock_data, name='get_stock_data'),
    path('get-graph/', views.get_graph_view, name='get_graph'),
    path('api/suggestions/', suggestions_view, name='suggestions'),
    path('setMonitor/', setMonitor, name= "setMonitor")
]