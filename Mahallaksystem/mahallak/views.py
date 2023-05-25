import http
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout

from .models import *


def calculate_new_price(old_price, discount):
    return old_price - old_price * (discount / 100)


class ProductOffer:
    def __init__(self, offer):
        self.product = offer.product
        self.new_price = calculate_new_price(self.product.price, offer.discount)


def index(request):
    data = {
        "user": request.user
    }
    if not request.user.is_authenticated:
        return redirect("login")
    categories_list = Category.objects.all()
    products_list = Product.objects.all()
    offers_list = Offer.objects.all()
    offers_list = [ProductOffer(offer) for offer in offers_list]
    data["offers"] = offers_list
    data["products"] = products_list
    data["categories"] = categories_list
    return render(request, "index.html", data)


def categories(request):
    data = {
        "user": request.user
    }
    categories_list = Category.objects.all()
    data["categories"] = categories_list
    return render(request, "categories.html",data)


def customize(request):
    if request.user.is_authenticated:
        a=0
        b=0
        for usr in Merchant.objects.all():
            if usr.user==request.user:
                a+=1
        if a :
            return render(request,"customize.html")
        else:
            return redirect("index")

def item(request):
    return render(request, "item.html")


def login_view(request: HttpRequest):
    if request.method == "POST":
        # check if user is already logged in
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            return render(request, "login.html", {"error": "Invalid username or password"})
        else:
            login(request, user)
            return redirect("index")
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def newitem(request):
    if request.user.is_authenticated:
        a=0
        b=0
        for usr in Merchant.objects.all():
            if usr.user==request.user:
                a+=1
        if a :
            return render(request,"newitem.html")
        else:
            return redirect("index")


def offers(request):
    data = {
        "user": request.user
    }
    offers_list = Offer.objects.all()
    data["offers"] = offers_list
    return render(request, "offers.html",data)


def products(request):
    return render(request, "products.html")


def register(request):
    if request.method =="POST":
        uservalue=request.POST.get("username")
        passwordvalue1=request.POST.get("password")
        passwordvalue2=request.POST.get("confirm password")
        emailvalue=request.POST.get("email")
        type=request.POST.get("type")
        address1=request.POST.get("address")
        bundle=request.POST.get("bundle")

        if passwordvalue1 == passwordvalue2:
                try:
                    user= User.objects.get(username=uservalue)
                    context= { 'error':'username already taken.'}
                    return render(request, 'register.html', context)
                except User.DoesNotExist:
                    user1= User.objects.create_user(uservalue, password= passwordvalue1, email=emailvalue)
                    if type == "c":
                        customer1=Customer.objects.create(user=user1,address=address1)
                        customer1.save()
                    else :
                        if bundle == "free":
                            merchant1=Merchant.objects.create(user=user1,address=address1,bundle="free")
                            merchant1.save()
                        elif bundle == "small":
                            merchant1=Merchant.objects.create(user=user1,address=address1,bundle="small")
                            merchant1.save()
                        else :
                            merchant1=Merchant.objects.create(user=user1,address=address1,bundle="large")
                            merchant1.save()
                    user1.save()   
                    

                    login(request, user1)
                    return render(request, 'index.html')
            
        else:
                context= { 'error':'The passwords don\'t match'}
                return render(request, 'register.html', context)

    else:
        return render(request, 'register.html')        
    
    


  


def store(request):
    return render(request, "store.html")


def stores(request):
    return render(request, "stores.html")
