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
    location = models.CharField(max_length=120)
    address = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.user} located in {self.location} address {self.address}"


class Category(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="categories", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=120)
    owner = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="stores")

    def __str__(self):
        return f"{self.name} located in {self.location} owned by {self.owner}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="products", null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="orders")


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.IntegerField()
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="details")


class Offer(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    discount = models.IntegerField()
