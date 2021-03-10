from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('diabApi.urls')) 
]
"""
What this means is that when the user makes a request with a url starting with http://127.0.0.1:8000/api..
it will redirect into 'dabApi.urls' module
"""