
from math import ceil
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render

from .forms import RegisterForm
from .models import Contact, Orders, Product
import json
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
   count = User.objects.count()
   return render(request, 'shop/index.html', {'count' : count})


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')




def productView(request, myid):

    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html', {'product':product[0]})


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')

def products(request):
    
    productos = Product.objects.all()
    if request.POST.get('menor'):
        productos = Product.objects.order_by('price')
    elif request.POST.get('mayor'):
        productos = Product.objects.order_by('-price')
    elif request.POST.get('Viajes'):
        productos = Product.objects.filter(category='Viajes')
    elif request.POST.get('Hoteleria'):
        productos = Product.objects.filter(category='Hoteleria')
    elif request.POST.get('Viajes_Hoteleria'):
        productos = Product.objects.filter(category='Viajes + Hoteleria')      
    else:
        productos = Product.objects.all()    
    return render(request, 'shop/products.html', {'productos':productos})

def signup(request):
    
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        

        user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        print('usuario creado')
        user.save();
        return redirect('/')
    else:
        return render(request, "registration/signup.html")
