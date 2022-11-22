from django.db import models
from datetime import datetime

# Create your models here.

class userSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    #created=models.DateTimeField(default=datetime.now(), blank=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    
class mynotes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    querytitle=models.CharField(max_length=200)
    cate=models.CharField(max_length=100)
    myfile=models.FileField(upload_to="MyNotes")
    comments=models.TextField()