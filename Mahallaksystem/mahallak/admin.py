from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Merchant)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Category)
admin.site.register(Offer)


