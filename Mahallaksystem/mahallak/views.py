import http
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import ProductForm


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
    return render(request, "categories.html", data)


def customize(request):
    merchant = get_object_or_404(Merchant, user=request.user)
    if request.method == "POST":
        pass
    else:
        store = merchant.stores.first()
        products = store.products.all()
        return render(request, "customize.html", {"merchant": merchant, "store": store, "products": products})


def item(request):
    return render(request, "item.html")


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
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print("RUNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNn")
            form.save()
            return redirect('.')
        else:
            print("ERRRRRRRRRRRRRRRRRRORRRRRRRRRRRRRRr")
    else :
        form = ProductForm()

    return render(request, "new-item.html", {'form': form})



def offers(request):
    data = {
        "user": request.user
    }
    offers_list = Offer.objects.all()
    data["offers"] = offers_list
    return render(request, "offers.html", data)


def products(request):
    return render(request, "products.html")


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
            merchant.save()
        login(request, user)
        if type == "merchant":
            return redirect("store")
        if type == "customer":
            return redirect("index")
    else:
        return render(request, 'register.html')


def store(request):
    return render(request, "store.html")


def stores(request):
    return render(request, "stores.html")
