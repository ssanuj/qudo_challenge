"""customers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import views as product_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('products/orders/', product_view.orders, name ='orders'),
    path('products/order_history/', product_view.order_history, name ='order_history'),
    path('products/signup/', product_view.signup, name ='signup'),
    path('products/signin/', product_view.signin, name = 'login'),
    path('products/signout/', product_view.signout, name = 'logout'),

]
