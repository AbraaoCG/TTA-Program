from django.urls import path,include
#from . import views
from .views import update_email, update_password, update_monitoring_period, login_user, register_user, logout_user

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('update-email/', update_email, name='update_email'),
    path('update-password/', update_password, name='update_password'),
    path('update-monitoring-period/', update_monitoring_period, name='update_monitoring_period'),
]