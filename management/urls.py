from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('product/groups/info/', views.productsGroup, name='product-group'),
    path('product/groups/products/', views.mainProduct, name='products'),
    path('product/groups/other/products/', views.otherProduct, name='other-products'),
    path('product/groups/sizes/', views.size, name='products-size'),
    path('product/search/', views.search, name='products-search'),
    path('user/register/', views.register, name='register'),
    path('user/logout/', views.logout, name='logout'),
    path('user/login/', views.login, name='login'),
    path('user/password/reminder/', views.passwordReminder, name='password-reminder'),
    path('user/user/info/', views.getUserInfo, name='user-info'),
    path('user/order/', views.order, name='order_content')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)