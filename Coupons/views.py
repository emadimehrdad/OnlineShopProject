from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import FormView

from Coupons.forms import CouponApplyForm
from Coupons.models import Coupon


class CouponView(FormView):
    form_class = CouponApplyForm
    now = timezone.now()

    def form_valid(self, form):
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=self.now,
                                        valid_to__gte=self.now)
            self.request.session['coupon_id'] = coupon.id

        except:
            self.request.session['coupon_id'] = None

        return super(CouponView, self).form_valid(form)
