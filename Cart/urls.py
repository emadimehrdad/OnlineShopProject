
from django.urls import path


from .views import CartAddProductView, CartDetailView, CartRemoveView

app_name = 'Cart'
urlpatterns = [
    path('', CartDetailView.as_view(), name="cart_detail"),
    path('add/<int:product_id>/', CartAddProductView.as_view(), name="cart_add"),
    path('remove/<int:product_id>/', CartRemoveView.as_view(), name="cart_remove"),
]
