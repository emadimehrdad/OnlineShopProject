from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import ProductDetailView, ProductListView, CategoryListView

app_name = 'Shop'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:category_slug>', CategoryListView.as_view(), name='category_list'),
    # path('', views.product_list, name='product_list'),
    # path('<slug:category_slug>', views.product_list, name='category_list'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
