import http

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout

from .models import Category, Product, Offer


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
    return render(request, "categories.html")


def customize(request):
    return render(request, "customize.html")


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
    return render(request, "newitem.html")


def offers(request):
    return render(request, "offers.html")


def products(request):
    return render(request, "products.html")


def register(request):
    return render(request, "register.html")


def store(request):
    return render(request, "store.html")


def stores(request):
    return render(request, "stores.html")
