from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product,Order


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
# view  available books for ordering
def orders(request):
    # check user authentications
    if request.user.is_authenticated:
        #get the available books to order
        order_list = Product.objects.all().filter(stock_quantity__gt=0).values('name','stock_quantity','price').order_by('name')
        context = {'order_list': order_list} 
        
        return render(request, "products/orders.html",context)
    else:
        return redirect('/products/signin')
# get the items that are checked
def place_order(request):
    if request.user.is_authenticated:    
        #get the username
        user = request.user.username
        #get the books to order
        items = request.POST.getlist('items[]')
        #get the item details
        item_details = Product.objects.filter(name__in=items).values_list('id','price')
        #book_names = []
        book_id = []
        total_amount = 0
        for row in item_details:
            # update the product table
            p = Product.objects.get(id=row[0])
            p.stock_quantity -= 1
            p.save()
            # create an entry in the orders table
            update_order = Order.objects.create(price=row[0],order_name=user,product=p)
            update_order.save()
        return redirect('/products')
    else:
        return redirect('/products/signin')
# retrieve the order hisroty for the user
def order_history(request):
    if request.user.is_authenticated:
        # get the product list from the product table
        order_history = Order.objects.all().values('product__name', 'price').filter(order_name=request.user.username).order_by('created_on')
        
        context = {
            'order_history': order_history
        }
    
        return render(request, "products/order_history.html", context)
     
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



