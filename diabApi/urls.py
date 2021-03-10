from django.urls import path
from diabApi import views

urlpatterns = [
    path('add/', views.api_add,name='api_add'),
]
"""
This is essentially the extension of the urls from the main project. So basically, 
what we are trying to achieve is that when a user sends a request starting with url
http://127.0.0.1:8000/api/add/,
run the function 'api_add' in the views.py inside the diabApi app. 

"""