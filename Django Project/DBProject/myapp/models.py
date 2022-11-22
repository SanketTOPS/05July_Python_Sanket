from django.db import models

# Create your models here.

class userdata(models.Model):
    name=models.TextField()
    email=models.EmailField()
    city=models.TextField()

    def __str__(self):
        return self.name