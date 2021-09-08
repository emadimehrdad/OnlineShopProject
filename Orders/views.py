from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from Cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem


class OrderCreateView(FormView):
    form_class = OrderCreateForm
    success_url = reverse_lazy("Orders:order_created")
    order = None

    def form_valid(self, form):
        cart = Cart(self.request)
        self.order = form.save()
        for item in cart:
            OrderItem.objects.create(order=self.order,
                                     product=item['product'],
                                     quantity=item['quantity'],
                                     price=item['price'])
        cart.clear()
        return super(OrderCreateView, self).form_valid(form)

    def get_success_url(self):
        product_id = self.order.id
        return reverse_lazy("Orders:order_created", kwargs={'product_id': product_id})

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data()
        context['order'] = self.order
        return context

    def get(self, request, *args, **kwargs):
        form = OrderCreateForm()
        cart = Cart(request)
        return render(request,
                      "orders/create.html",
                      {'form': form, 'cart': cart})


class OrderCreatedView(TemplateView):
    template_name = "orders/created.html"

    def get_context_data(self, **kwargs):
        context = super(OrderCreatedView, self).get_context_data()
        context['order'] = self.kwargs['product_id']
        return context