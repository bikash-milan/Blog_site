from django.db import models
from matplotlib.pyplot import title
from django.contrib.auth.models import User
# Create your models here.

class blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=20)
    desc = models.CharField(max_length=20000)
    img = models.ImageField(upload_to='dp')
    

    def __str__(self):
        return self.author.username


# class blog(models.Model):
#     image = models.ImageField
#     heading=models.CharField(max_length=50)
#     descrp= models.CharField(max_length=5000)