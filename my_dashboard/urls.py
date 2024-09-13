from django.urls import path, include
from . import views
from .views import suggestions_view,setMonitor,get_stock_monitors,update_monitor,delete_monitor

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('get-stock-data/', views.get_stock_data, name='get_stock_data'),

    path('get-graph/', views.get_graph_view, name='get_graph'),

    path('api/suggestions/', suggestions_view, name='suggestions'),

    path('setMonitor/', setMonitor, name= "setMonitor"),
    path('set-monitor/', views.setMonitor, name='setMonitor'),

    path('get-stock-monitors/', get_stock_monitors, name='get_stock_monitors'),
    path('update-monitor/', update_monitor, name='update_monitor'),
    path('delete-monitor/', delete_monitor, name='delete_monitor'),
]