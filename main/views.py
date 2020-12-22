from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request,'home.html')

def collection(request):
   return render(request,'collection.html')


def productdetails(request):
   return render(request,'product-details.html')
