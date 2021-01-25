from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/images')
    price = models.FloatField()
    delprice= models.FloatField()
    category=models.CharField(max_length=100,null=True)
    brand=models.CharField(max_length=100,null=True)
    color=models.CharField(max_length=100,null=True)
    slug=models.SlugField(max_length=200,unique=True,null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
