from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #parent = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name='children')
    school_name = models.CharField(max_length=256)
    standard = models.CharField(max_length=50)
    points = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username
    

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username