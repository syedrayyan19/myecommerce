from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('collection',views.collection,name='collection'),
    path('product-details',views.productdetails,name='product-details')
]
