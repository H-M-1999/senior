from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
import random
from .models import *
from django.core.files.storage import FileSystemStorage

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
    categories_list = random.sample(list(Category.objects.all()), 3)
    products_list = Product.objects.all()
    offers_list = Offer.objects.all()
    offers_list = [ProductOffer(offer) for offer in offers_list]
    data["offers"] = offers_list
    data["products"] = products_list
    data["categories"] = categories_list
    return render(request, "index.html", data)


def categories(request):
    data = {
        
    }
    categories_list = Category.objects.all()
    data["categories"] = categories_list
    return render(request, "categories.html", data)


def customize(request):
    merchant = get_object_or_404(Merchant, user=request.user)
    if request.method == "POST" and request.FILES['upload']:
        upload=request.FILES['upload']
        fss= FileSystemStorage()
        file=fss.save(upload.name,upload)
        file_url=fss.url(file)
        store = merchant.stores.first()
        store.image=file_url
        store.name = request.POST.get("name")
        store.location = request.POST.get("location")
        store.save()
        return redirect('customize')
    else:
        store = merchant.stores.first()
        products = store.products.all()
        return render(request, "customize.html", {"merchant": merchant, "store": store, "products": products})
# orderdetails = Order.details.all().delete()

def item(request,name):
    product=Product.objects.get(name=name)
    similar=Product.objects.filter(category=product.category)
    if request.method == "POST":
        order,_= Order.objects.get_or_create(customer=request.user, store=product.store)
        order_detail=OrderDetail.objects.create(product=product,price=product.price,order=order)
        return render(request, "cart.html",{"product":product,"order":order,"order_detail":order_detail})
       
    else:  
        return render(request, "item.html",{"product":product,"similar":similar})


def login_view(request: HttpRequest):
    if request.method == "POST":
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


def new_item(request):
     merchant = get_object_or_404(Merchant, user=request.user)
     categories=Category.objects.all()
     if request.method == "POST" and request.FILES['upload']:
        upload=request.FILES['upload']
        fss= FileSystemStorage()
        file=fss.save(upload.name,upload)
        file_url=fss.url(file)
        image=file_url
        discount=request.POST.get("discount")
        name = request.POST.get("product_name")
        price= request.POST.get("product_price")
        category=request.POST.get("category")
        descrpition=request.POST.get("product_description")
        product=Product(name=name,description=descrpition,image=image,price=price,store=merchant.stores.first(),category=Category.objects.filter(name=category).first())
        product.save()
        if int(discount) != 0 :
            offer=Offer(product=product,discount=discount)
            offer.save()
        return redirect("new_item")
     else:
        return render(request,"new-item.html",{'categories':categories})



def offers(request):
    data = {
        "user": request.user
    }
    offers_list = Offer.objects.all()
    data["offers"] = offers_list
    return render(request, "offers.html", data)


def products(request):
    data = {
        
    }
    offers = Offer.objects.all()
    ofp_id = [offer.product.pk for offer in offers]
    products_list = Product.objects.filter().exclude(id__in=ofp_id)
    data["products"] = products_list
    return render(request, "products.html", data)


def register(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("confirm password")
        email = request.POST.get("email")
        type = request.POST.get("type")
        address = request.POST.get("address")
        bundle = request.POST.get("bundle")

        if password != password_confirm:
            return render(request, 'register.html', {"error": "Passwords don't match"})
        if User.objects.filter(username=user).exists():
            return render(request, 'register.html', {"error": "Username already exists"})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {"error": "Email already exists"})
        if type not in ("merchant", "customer"):
            return render(request, 'register.html', {"error": "Invalid type"})
        if type == "merchant" and bundle not in ("free", "small", "large"):
            return render(request, 'register.html', {"error": "Invalid bundle"})

        # valid data
        user = User.objects.create_user(username=user, password=password, email=email)
        user.save()
        if type == "customer":
            customer = Customer(user=user, address=address)
            customer.save()
        if type == "merchant":
            merchant = Merchant(user=user, address=address, bundle=bundle)
            owns=Store(name=" ", location=merchant.address, owner=merchant)     
            merchant.save()
            owns.save()
           
        login(request, user)
        if type == "merchant":
            return redirect("store")
        if type == "customer":
            return redirect("index")
    else:
        type=request.POST.get("type")
        return render(request, 'register.html',{"type":type})


def store(request,name):
    store=Store.objects.get(name=name)
    product_list=store.products.all()
    offers = Offer.objects.filter(product__in=product_list)
    offer_list=[ProductOffer(offer) for offer in offers]
    return render(request, "store.html",{"store":store,"products":product_list,"offers":offer_list,"user":request.user})    


def stores(request):
    data = {
        
    }
    stores_list = Store.objects.all()
    data["stores"] = stores_list
    return render(request, "stores.html", data)

def cart(request):

    return render(request,"cart.html")