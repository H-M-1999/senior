from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Merchant(models.Model):
    choices = (
        ("free", "free"),
        ("small", "small"),
        ("large", "large"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="merchant")
    bundle = models.CharField(max_length=20, choices=choices)
    address = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.user} owns {self.bundle} bundle located in {self.address}"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    address = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.user} located in {self.address}"


class Category(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="categories", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Store(models.Model):
    name = models.CharField(max_length=100,unique=True)
    location = models.CharField(max_length=120)
    owner = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="stores")
    image=models.ImageField(upload_to="stores",null=True, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.name} located in {self.location} owned by {self.owner}"


class Product(models.Model):
    name = models.CharField(max_length=100 )
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="productsinit")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="products", null=True, blank=True)
    description = models.TextField(max_length=500,default="")


class Order(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name="orders")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="orders")


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.IntegerField(default=0)
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="details")


class Offer(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,related_name="offer")
    discount = models.IntegerField()
