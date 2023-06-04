from django.contrib import admin
from django.urls import include, path
from .store.views import *

urlpatterns = [
    path('products/', get_products),
    path('categories/', get_categories),
    path('product/<slug:product_slug>/<slug:color_slug>/', get_product),
]