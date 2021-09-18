
from django.urls import path

from .views import CouponApplyView, remove_coupon

app_name = 'Coupons'
urlpatterns = [
    path('apply', CouponApplyView.as_view(), name="coupon_apply"),
    path('remove', remove_coupon, name="coupon_remove"),
]
