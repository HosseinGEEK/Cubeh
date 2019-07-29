from django.contrib import admin
from .models import Group, Product, OtherProduct, Size, Order, User
# Register your models here.

admin.site.register(Group)
admin.site.register(Product)
admin.site.register(OtherProduct)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(User)