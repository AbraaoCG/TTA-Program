from django.urls import path,include
#from . import views
from .views import update_email, update_password, update_monitoring_period, login_user, register_user

urlpatterns = [
    path('login/', login_user, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('register/', register_user, name='register'),
    path('update-email/', update_email, name='update_email'),
    path('update-password/', update_password, name='update_password'),
    path('update-monitoringPeriod/', update_monitoring_period, name='update_monitoring_period'),
]