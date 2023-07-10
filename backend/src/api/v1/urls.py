from django.urls import path
from .store.views import *
from .coupon.views import *

urlpatterns = [
    path('products/', get_products),
    path('products/<slug:category_slug>/', get_products),
    path('categories/', get_categories),
    path('products/<slug:product_slug>/<slug:color_slug>/', get_product),
    path('products/<slug:product_slug>/<slug:color_slug>/<str:size>/', get_product_on_size),
    path('products/<slug:product_slug>/<slug:color_slug>/<str:size>/supply/', get_supply),
    path('coupon/<slug:coupon>/', check_coupon),
    # path('coupon/<slug:coupon>/', use_coupon)
]
