from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import pickle
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np
import pandas as pd
# custom
from .apps import DiabapiConfig
from .models import Diabetes

# Function based view to add numbers
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


# Class based view to add numbers
class Add_Values(APIView):
    def post(self, request, format=None):
        sum = 0
        # Add the numbers
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
        return Response(response_dict, status=status.HTTP_201_CREATED)

# Class based view to predict based on diabetes model
class Deabetes_Model_Predict(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data_dict = request.data

        keys=[]
        values=[]
        for key in data_dict:
            keys.append(key)
            values.append(data_dict[key])
        
        values_nparray = np.array(values)
        # print(values_nparray)
 
        scaler = DiabapiConfig.scaler
        # print(scaler)
        scaled_data = scaler.transform(values_nparray.reshape(1,-1))
        # print(scaled_data)

        prediction = DiabapiConfig.classifier.predict(scaled_data)
        print(prediction)
        if prediction == 1:
            result = "Diabetes Detected"
        else:
             result = "No Diabetics"

        # Add data to db
        obj = Diabetes()
        obj.Pregnancies = values[0]
        obj.Glucose = values[1]
        obj.BloodPressure = values[2]
        obj.SkinThickness = values[3]
        obj.Insulin = values[4]
        obj.BMI = values[5]
        obj.DiabetesPedigreeFunction = values[6]
        obj.Age = values[7]
        obj.Prediction = result
        obj.save()

        



        
        return Response(result,status=200)

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