
from django.urls import path

from .views import OrderCreateView, OrderCreatedView

app_name = 'Orders'
urlpatterns = [
    path('create/', OrderCreateView.as_view(), name="order_create"),
    path('created/<int:product_id>', OrderCreatedView.as_view(), name="order_created"),
]
