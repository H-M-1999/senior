from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("offers", views.offers, name="offers"),
    path("products", views.products, name="products"),
    path("new_item", views.new_item, name="new_item"),
    path("products/<str:name>", views.item, name="item"),
    path("stores/<str:name>", views.store, name="store"),
    path("stores", views.stores, name="stores"),
    path("customize", views.customize, name="customize"),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("register", views.register, name="register"),
    path("cart", views.cart, name="cart"),
    path("cart/delete/<int:id>", views.delete, name="delete"),
    path("add_to_cart/<int:id>", views.add_to_cart, name="add_to_cart"),
    path("cart/checkout", views.checkout, name="checkout"),
    path("categories/<str:name>", views.by_category, name="category"),
    path("customize/sent/<int:id>",views.sent,name="sent"),
    path("customize/delete/<int:id>",views.delete_product,name="delete_product"),
]
