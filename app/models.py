from django.contrib.auth.models import User
from django.db import models

class School(models.Model):
    code = models.CharField(max_length=100, unique=True)

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)