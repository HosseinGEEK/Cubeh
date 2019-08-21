from django.contrib import admin
from .models import Group, Product, Size, Order, User, Question, Ticket, LatestNews, Slider
# Register your models here.

admin.site.register(Group)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Ticket)
admin.site.register(LatestNews)
admin.site.register(Slider)