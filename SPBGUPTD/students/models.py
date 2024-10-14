from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=10)
    specialization = models.TextField()