from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/images')
    price = models.FloatField()
    delprice= models.FloatField()
    category=models.CharField(max_length=100,null=True)
    brand=models.CharField(max_length=100,null=True)
    color=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
