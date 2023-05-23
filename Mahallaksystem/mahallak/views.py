from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   return render(request, "index.html")

def categories(request):
   return render(request, "categories.html")

def customize(request):
   return render(request, "customize.html")

def item(request):
   return render(request, "item.html")

def login(request):
   return render(request, "login.html")

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
