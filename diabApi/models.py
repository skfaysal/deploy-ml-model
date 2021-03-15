from django.db import models

# Create your models here.

class Diabetes(models.Model):
    Pregnancies = models.CharField(max_length=200, blank=True)
    Glucose = models.CharField(max_length=200, blank=True)
    BloodPressure = models.CharField(max_length=200, blank=True)
    SkinThickness = models.CharField(max_length=200, blank=True)
    Insulin = models.CharField(max_length=200, blank=True)
    Insulin = models.CharField(max_length=200, blank=True)
    BMI = models.CharField(max_length=200, blank=True)
    DiabetesPedigreeFunction = models.CharField(max_length=200, blank=True)
    Age = models.CharField(max_length=200, blank=True)
    Prediction = models.CharField(max_length=200, blank=True)

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()