from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product


# display the list of the products if the user authentication is a success
def products(request):
    if request.user.is_authenticated:
        # get the product list from the product table
        prod_list = Product.objects.all().values('name', 'price','stock_quantity').order_by('name')
        paginator = Paginator(prod_list, 4)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
        context = {
            'products': products
        }
    
        return render(request, "products/products.html", context)
     
    else:
        return redirect('/products/signin')
# Place orders by listing the available books
def orders(request):
    # check user authentications
    if request.user.is_authenticated:
        #get the available books to order
        available_books = Product.obejects.filter()
        context = {}
        return render(request, "products/orders.html",context)
    else:
        return redirect('/products/signin')
        
def signup(request):
 
    if request.user.is_authenticated:
        return redirect('/products')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/products')
         
        else:
            return render(request,'products/signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'products/signup.html',{'form':form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('/products')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/products')
        else:
            form = AuthenticationForm()
            return render(request,'products/signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'products/signin.html', {'form':form})
 
 
def signout(request):
    logout(request)
    return redirect('/products/signin/')



