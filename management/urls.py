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
    path('product/update/unitPrice/', views.update_unit_price, name='products-update-price'),
    path('product/compare/', views.product_compare, name='products-compare'),
    path('user/register/', views.register, name='register'),
    path('user/logout/', views.logout, name='logout'),
    path('user/login/', views.login, name='login'),
    path('user/password/reminder/', views.password_reminder, name='password-reminder'),
    path('user/update/profile/', views.update_profile, name='update-profile'),
    path('user/profile/info/', views.user_info, name='user-profile-info'),
    path('user/order/', views.order, name='order_content'),
    path('support/questions/', views.question, name='frequently-asked-questions'),
    path('support/latestnews/', views.latest_new, name='latest-news'),
    path('support/ticket/', views.ticket, name='ticket'),
    path('support/slider/', views.slider, name='slider'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#SERVER PASSWORD: aXVfT#kPumKN 
#GIT URL FOR PULL: https://github.com/HosseinGEEK/Cubeh.git