
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('employees/', include('employees.urls')),
    path('admin/', admin.site.urls),
]
