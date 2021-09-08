from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DeleteView, DetailView, TemplateView

from Shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
# Create your views here.


class CartAddProductView(FormView):
    form_class = CartAddProductForm
    template_name = "cart/cart_detail.html"
    success_url = reverse_lazy("Cart:cart_detail")
    product = None

    def form_valid(self, form):
        self.product = get_object_or_404(Product, id=self.kwargs['product_id'])
        cart = Cart(self.request)
        cart.add(product=self.product,
                 quantity=form.cleaned_data['quantity'],
                 override_quantity=form.cleaned_data['override'])
        return super(CartAddProductView, self).form_valid(form)


class CartRemoveView(View):

    def post(self, request):
        product_id = request.POST.get('product_id')
        product = Product.objects.filter(id=product_id)
        cart = Cart(request)
        cart.remove(product)
        return redirect('Cart:cart_detail')


class CartDetailView(TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data()
        context['cart'] = cart
        return context
