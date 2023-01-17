# Use include() to add paths from the catalog application
from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    
    path('',views.products, name='products'),
   
]
    
