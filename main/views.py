from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
   products=Products.objects.all()
   return render(request,'home.html',{'products':products})

def collection(request):
   return render(request,'collection.html')


def productdetails(request,slug):
   sl=Products.objects.get(slug=slug)
   
   return render(request,'product-details.html',{'sl':sl})

def checkout(request):
   return render(request,'checkout.html')
