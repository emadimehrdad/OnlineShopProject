from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/product_list.html'
    context_object_name = "product_list"

    def get_queryset(self, **kwargs):
        context = Product.objects.filter(available=True)
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryListView(ListView):
    model = Product
    template_name = 'shop/product/product_list.html'

    def get_queryset(self, **kwargs):
        context = Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True)
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if self.kwargs['category_slug']:
            context['category'] = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product/product_detail.html"
    queryset = Product.objects.filter(available=True)
    context_object_name = "product"