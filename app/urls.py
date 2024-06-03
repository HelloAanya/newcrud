from django.contrib import admin
from django.urls import path, include
from app import urls   # Fix the import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('myapp/', include('app.urls')),
    
]
