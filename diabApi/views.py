from django.shortcuts import render
import pickle
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np

# Create your views here.
@api_view(['GET', 'POST']) # A Decorator to define an API function in Django. It's converts  python function into API function
def api_add(request):
    sum = 0
    response_dict = {}
    if request.method == 'GET':
        # Do nothing
        pass
    elif request.method == 'POST':
        # Add the numbers
        data = request.data
        print(data)
        print(type(data))
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
    return Response(response_dict, status=status.HTTP_201_CREATED)


"""
This  response dictionary is then sent back with the Response function 
(imported from the Response module of the django rest framework). 
The Response function is a highly versatile function and it determines 
the rendered output type of the response data on the fly. This is determined 
by a content negotiation with the client application 
(i.e. web browser, mobile app etc.). 
So, if the client application requires output in the form of a JSON, 
the Response function would convert the data to JSON in the output. 
This is why we are able to send a Python dictionary as output with the Response. 
You can read more about the Response function from the official documentation. 
"""