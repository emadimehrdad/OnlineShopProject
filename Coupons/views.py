from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import FormView, TemplateView

from Cart.cart import Cart
from Coupons.forms import CouponApplyForm
from Coupons.models import Coupon


class CouponApplyView(FormView):
    form_class = CouponApplyForm
    now = timezone.now()
    success_url = reverse_lazy("Cart:cart_detail")

    def form_valid(self, form):
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=self.now,
                                        valid_to__gte=self.now)
            self.request.session['coupon_id'] = coupon.id

        except:
            self.request.session['coupon_id'] = None

        return super(CouponApplyView, self).form_valid(form)


def remove_coupon(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart.remove_coupon()
        return redirect("Cart:cart_detail")

    return render("Cart:cart_detail")
