from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from my_dashboard.views import dashB_redirect 

urlpatterns = [
    path('', dashB_redirect, name = 'dashboard'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('my_dashboard.urls')),
    path('auth/', include('users.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)