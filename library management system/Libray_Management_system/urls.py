from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('library.urls')),
    path("admin_users/",include('django.contrib.auth.urls')),
    path("admin_users/",include('admin_users.urls')),
]
