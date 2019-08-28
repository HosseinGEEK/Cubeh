from django.core.files.storage import FileSystemStorage
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
    brand = models.CharField(max_length=10, choices=brands, blank=True, null=True)
    types = (('main', 'main'), ('other', 'other'))
    type = models.CharField(max_length=5, choices=types)

    def __str__(self):
        if self.brand == 'easy':
            b = 'ایزی پایپ'
        elif self.brand == 'new':
            b = 'نیو پایپ'
        else:
            b = 'ایساتیس'
        return self.group.name + '-->' + self.name + '-->' + b


class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=15)
    code = models.CharField(max_length=12)
    price = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.code + '-->' + self.product.name + '-->' + self.size + '-->' \
               + str(self.discount) + '-->' + str(self.price)


class User(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=40)
    phone_number = models.CharField(primary_key=True, max_length=11)
    password = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    image_path = models.CharField(null=True, blank=True, max_length=200)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    join_date = models.CharField(default=jalali.Gregorian(datetime.now().date()).persian_string(), max_length=20,
                                 editable=False)

    # last_seen = models.CharField(max_length=20, editable=False)

    def __str__(self):
        return self.fname + ' ' + self.lname + '، تاریخ ثبت نام: ' \
               + self.join_date


class Order(models.Model):
    order_number = models.CharField(primary_key=True, unique=True, max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    total_price = models.CharField(max_length=15)
    order_record_date = models.CharField(default=jalali.Gregorian(datetime.now().date()).persian_string(),
                                         max_length=20, editable=False)

    def __str__(self):
        return self.user.phone_number + '-->' + self.order_record_date


class Question(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    explanation = models.TextField()
    rating = models.CharField(max_length=5)
    problem = models.BooleanField(default=False)

    def __str__(self):
        return self.user.lname + ' ' + self.title


class Slider(models.Model):
    image_url = models.CharField(max_length=200)


class LatestNews(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
