from django.db import models
from datetime import datetime
from . import jalali


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=50)
    group_name = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=50)
    priority = models.IntegerField()
    brands = (('easy', 'ایزی پایپ'), ('new', 'نیو پایپ'), ('ica', 'ایساتیس'))
    brand = models.CharField(max_length=10, choices=brands)

    def __str__(self):
        if self.brand == 'easy':
            b = 'ایزی پایپ'
        elif self.brand == 'new':
            b = 'نیو پایپ'
        else:
            b = 'ایساتیس'
        return self.group.name + '-->' + self.name + '-->' + b


class OtherProduct(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=50)
    priority = models.IntegerField()
    brands = (('easy', 'ایزی پایپ'), ('new', 'نیو پایپ'), ('isa', 'ایساتیس'))
    brand = models.CharField(max_length=10, choices=brands)

    def __str__(self):
        if self.brand == 'easy':
            b = 'ایزی پایپ'
        elif self.brand == 'new':
            b = 'نیو پایپ'
        else:
            b = 'ایساتیس'
        return self.group.name + '-->' + self.name + '-->' + b


class Size(models.Model):
    main_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    other_product = models.ForeignKey(OtherProduct, on_delete=models.CASCADE, null=True, blank=True)
    size = models.CharField(max_length=15)
    code = models.CharField(max_length=12)
    price = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        product_name = ''
        if self.main_product != None:
            product_name = self.main_product.name
        elif self.other_product != None:
            product_name = self.other_product.name
        return self.code + '-->' + product_name + '-->' + self.size + '-->' \
               + self.discount + '-->' + str(self.price)


class User(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=40)
    phone_number = models.CharField(primary_key=True, max_length=11)
    password = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    join_date = models.DateTimeField(default=datetime.now(), editable=False)
    last_seen = models.CharField(max_length=20, editable=False)

    def __str__(self):
        return self.fname + ' ' + self.lname + '، تاریخ ثبت نام: ' \
               + jalali.Gregorian(self.join_date.date()).persian_string()


class Order(models.Model):
    order_number = models.IntegerField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
	#add field total product and price
    content = models.TextField()
    order_record_date = models.CharField(default=jalali.Gregorian(datetime.now().date()).persian_string() ,max_length=20, editable=False)

    def __str__(self):
        return self.user.phone_number + '-->' + self.order_record_date

