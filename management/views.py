from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Order, Group, Product, OtherProduct, Size
from json import dumps, loads
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    return HttpResponse('<h1>This Is Managerial Panel For Cubeh Application </h1>')


def productsGroup(request):
    groups = []
    group = Group.objects.all()
    for g in group:
        context = {
            'name': g.name,
            'image_url': g.image_url
        }
        groups.append(context)

    return HttpResponse(dumps(groups))


# post a group_name and key of brands
@csrf_exempt
def mainProduct(request):
    group = []
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            g_name = info[0]
            brand = info[1]
            products = Product.objects.filter(group__name=g_name, brand=brand).order_by('priority')
            for p in products:
                context = {
                    'name': p.name,
                    'image_url': p.image_url,
                }
                group.append(context)
        except:
            return HttpResponse('<h1>:)</h1>')

    return HttpResponse(dumps(group))


# post a group_name and key of brands
@csrf_exempt
def otherProduct(request):
    group = []
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            g_name = info[0]
            brand = info[1]
            products = OtherProduct.objects.filter(group__name=g_name, brand=brand).order_by('priority')
            for p in products:
                context = {
                    'name': p.name,
                    'image_url': p.image_url,
                }
                group.append(context)
        except:
            return HttpResponse('<h1>:)</h1>')

    return HttpResponse(dumps(group))


@csrf_exempt
def size(request):
    group = []
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            product_type = info[0]
            product_name = info[1]
            if product_type == 'main':
                sizes = Size.objects.filter(main_product__name=product_name)
            else:
                sizes = Size.objects.filter(other_product__name=product_name)

            for s in sizes:
                context = {
                    'size': s.size,
                    'code': s.code,
                    'price': s.price,
                    'discount': s.discount
                }
                group.append(context)
        except:
            return HttpResponse('<h1>:)</h1>')

    return HttpResponse(dumps(group))


@csrf_exempt
def order(request):
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            phone_num = info['phone_number']
            user = User.objects.get(phone_number=phone_num)
            content = info['order_content']
            number = info['order_number']
            o = Order(order_number=number, user=user, content=content)
            o.save(force_insert=True)
            return HttpResponse(dumps({"record": "1"}))
        except:
            return HttpResponse(dumps({"record": "0"}))

    return HttpResponse('<h1>:)</h1>')


@csrf_exempt
def search(request):
    products = []
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            pName = info[0]
            mainProducts = Product.objects.filter(name=pName).order_by('priority')
            otherProducts = OtherProduct.objects.filter(name=pName).order_by('priority')

            for p in mainProducts:
                context = {
                    'name': p.name,
                    'image_url': p.image_url,
                    'brand': p.brand
                }
                products.append(context)
            for p in otherProducts:
                context = {
                    'name': p.name,
                    'image_url': p.image_url,
                    'brand': p.brand
                }
                products.append(context)

            return HttpResponse(dumps(products))
        except:
            return HttpResponse('<h1>:)</h1>')
    return HttpResponse('<h1>:)</h1>')


@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            fname = info['fname']
            lname = info['lname']
            phone_num = info['phone_number']
            password = info['password']
            user = User(fname=fname, lname=lname, phone_number=phone_num, password=password)
            user.save(force_insert=True)
            return HttpResponse(dumps({"register": "1"}))
        except:
            return HttpResponse(dumps({"register": "0"}))
    return HttpResponse('<h1>:)</h1>')


# todo set last seen
@csrf_exempt
def logout(request):
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            phone_num = info['phone_number']
            user = User.objects.filter(phone_number=phone_num)
            user.update(status=False)

            return HttpResponse(dumps("خروج با موفقیت صورت پذیرفت."))
        except:
            return HttpResponse('<h1>:)</h1>')
    return HttpResponse('<h1>:)</h1>')


# todo update last seen
@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            phone_num = info['phone_number']
            user = User.objects.filter(phone_number=phone_num)

            if len(user) > 0:
                password = info['password']
                if user[0].password == password:
                    user.update(status=True)
                    return HttpResponse(dumps({"login":"1"}))
                else:
                    return HttpResponse(dumps({"login":"2"}))
            else:
                return HttpResponse(dumps({"login":"0"}))
        except:
            return HttpResponse('<h1>:)</h1>')
    return HttpResponse('<h1>:)</h1>')


@csrf_exempt
def passwordReminder(request):
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            phone_num = info['phone_number']
            user = User.objects.filter(phone_number=phone_num)

            if len(user) > 0:
                password = user[0].password
                return HttpResponse(dumps("پنل پیامکی"))
            else:
                return HttpResponse(dumps("چنین کاربری وجود ندارد!!!"))
        except:
            return HttpResponse('<h1>:)</h1>')
    return HttpResponse('<h1>:)</h1>')


@csrf_exempt
def getUserInfo(request):
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            phone_num = info[0]
            user = User.objects.filter(phone_number=phone_num)
            if len(user) != 0:
                u = user[0]
                if u.status:
                    context = {
                        'fname': u.fname,
                        'lname': u.lname,
                        'phone_number': u.phone_number,
                        'email': u.email,
                        'date_of_birth': u.date_of_birth
                    }
                    return HttpResponse(dumps(context))
                else:
                    return HttpResponse(dumps("ابتدا وارد پنل خود شوید!"))
            else:
                return HttpResponse(dumps("ابتدا ثبت نام کنید!"))
        except:
            return HttpResponse('<h1>:)</h1>')
    return HttpResponse('<h1>:)</h1>')