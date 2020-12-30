from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('collection',views.collection,name='collection'),
    path('product-details/<str:slug>/',views.productdetails,name='product-details'),
    path('checkout',views.checkout,name='checkout')
]
