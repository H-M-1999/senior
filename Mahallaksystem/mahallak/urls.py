from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("offers", views.offers, name="offers"),
    path("products", views.products, name="products"),
    path("newitem", views.newitem, name="newitem"),
    path("item", views.item, name="item"),
    path("store", views.store, name="store"),
    path("stores", views.stores, name="stores"),
    path("customize", views.customize, name="customize"),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("register", views.register, name="register")
]
