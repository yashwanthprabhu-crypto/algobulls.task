from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('api/', include('tasks.urls')),  # Include the `tasks` app URLs
]
