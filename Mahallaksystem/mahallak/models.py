from django.db import models

# Create your models here.
class Merchant(models.Model):
    m_name=models.CharField(max_length=40)
    bundle=models.IntegerField()
    m_email=models.EmailField(default=" ")
    m_pass=models.CharField(max_length=40, default="NULL")
    m_address=models.CharField(max_length=120)
    def __str__(self):
        return f"{self.m_name}"
    

class Categorie(models.Model):
    cat_name=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.cat_name}"
    
class Store(models.Model):
    s_name=models.CharField(max_length=20)
    s_location=models.CharField(max_length=120)
    s_category=models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="soldat")
    s_owner=models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="owns")

    def __str__(self):
        return f"{self.s_name} located in {self.s_location} owned by {self.s_owner} sells {self.s_speciality}"


class Customer(models.Model):
    c_name=models.CharField(max_length=20)
    c_location=models.CharField(max_length=120)
    c_email=models.EmailField(default="")
    c_pass=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.c_name} located in {self.s_location}"


class Product(models.Model):
    p_name=models.CharField(max_length=20)
    p_price=models.FloatField()
    p_category=models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name="isa")
    p_store=models.ForeignKey(Store, on_delete=models.CASCADE, related_name="owns")
    def __str__(self):
        return f"{self.p_name} sells for {self.p_price} is a {self.p_category} sold at {self.p_store}"


class Order(models.Model):
    o_products=models.ManyToManyField(Product,blank=False, related_name="isin" )
    o_address=models.CharField(max_length=120)
    o_price=models.FloatField()
    o_owner=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="buying")
    def __str__(self):
        return f"{self.id} to deliver to {self.o_address} owned by {self.o_owner} sells for {self.o_price} contains{self.o_products}"



