
from django.urls import path
from onlineShop.views import index, detail, checkout, confirmation

urlpatterns = [
    path('', index, name='home'),
    path('<int:product_id>', detail, name='detail'),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation"),
]