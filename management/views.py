from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Order, Group, Product, Size
from json import dumps, loads
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    return HttpResponse('<h1>This Is Managerial Panel For Cubeh Application </h1>')


def products_group(request):
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
def product(request):
    group = []
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            g_name = info[0]
            brand = info[1]
            type = info[2]
            products = Product.objects.filter(group__name=g_name, brand=brand, type=type).order_by('priority')
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
            product_name = info[0]
            sizes = Size.objects.filter(product__name=product_name)

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
            number = info['order_number']
            content = info['order_content']
            total_p = info['total_price']
            o = Order(order_number=number, user=user, content=content, total_price=total_p)
            o.save(force_insert=True)
            return HttpResponse(dumps({"record": "1"}))
        except:
            return HttpResponse(dumps({"record": "0"}))

    return HttpResponse('<h1>:)</h1>')


@csrf_exempt
def search(request):
    group = []
    if request.method == "POST":
        try:
            info = loads(request.body.decode('utf-8'))
            p_name = info[0]
            products = Product.objects.filter(name__contains=p_name).order_by('priority')

            for p in products:
                context = {
                    'name': p.name,
                    'image_url': p.image_url,
                    'brand': p.brand
                }
                group.append(context)

            return HttpResponse(dumps(group))
        except:
            return HttpResponse('<h1>:)</h1>')
    return HttpResponse('<h1>:)</h1>')


@csrf_exempt
def update_unit_price(request):
    group = []
    try:
        if request.method == "POST":
            info = loads(request.body.decode('utf-8'))
            for s in info:
                size = Size.objects.filter(code=s)
                if len(size) != 0:
                    price = size[0].price
                    dis = size[0].discount
                    context = {
                        'price': price,
                        'discount': dis
                    }

                    group.append(context)
            return HttpResponse(dumps(group))
    except:
        return HttpResponse('<h1>:)</h1>')

    return HttpResponse('<h1>:)</h1>')


def product_compare(request):
    group = []
    if request.method == "POST":
        info = loads(request.body.decode('utf-8'))
        p_name = info[0]
        p_size = info[1]

        sizes = Size.objects.filter(product__name=p_name, size=p_size)
        for s in sizes:
            context = {
                "product_name": s.product.name,
                "size": s.size,
                "code": s.code,
                "price": s.price,
                "dis": s.discount,
                "brand": s.product.brand
            }

            group.append(context)
        return HttpResponse(dumps(group))

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
                    return HttpResponse(dumps({"login": "1"}))
                else:
                    return HttpResponse(dumps({"login": "2"}))
            else:
                return HttpResponse(dumps({"login": "0"}))
        except:
            return HttpResponse('<h1>:)</h1>')
    return HttpResponse('<h1>:)</h1>')


@csrf_exempt
def password_reminder(request):
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
def get_user_info(request):
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
