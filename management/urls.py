from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('product/groups/info/', views.products_group, name='product-group'),
    path('product/groups/products/', views.product, name='products'),
    path('product/groups/sizes/', views.size, name='products-size'),
    path('product/search/', views.search, name='products-search'),
    path('product//update/unitPrice/', views.update_unit_price, name='products-update-price'),
    path('user/register/', views.register, name='register'),
    path('user/logout/', views.logout, name='logout'),
    path('user/login/', views.login, name='login'),
    path('user/password/reminder/', views.password_reminder, name='password-reminder'),
    path('user/user/info/', views.get_user_info, name='user-info'),
    path('user/order/', views.order, name='order_content')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)