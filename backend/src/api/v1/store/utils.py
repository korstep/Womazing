from rest_framework import status

from apps.store.models import ProductColorImage, ProductSizeColor
from django.db.models import Subquery
from django.db.models import Q
from rest_framework.response import Response

sort_by_settings = {
    '0': '-product_id',
    '1': 'product__price',
    '2': '-product__price'
}

default_sort_by = '0'


def get_products_data(category_slug=None, count=None, sort_by=None):
    products = products_on_sale()
    if category_slug:
        products = products.filter(product__category__slug=category_slug)

    if sort_by and sort_by in sort_by_settings:
        sort_field = sort_by_settings[str(sort_by)]
        products = products.order_by(sort_field)
    else:
        sort_field = sort_by_settings[default_sort_by]
        products = products.order_by(sort_field)

    if count:
        products = products.distinct('product_id')[:int(count)]

    return products


def products_on_sale():
    product_ids = ProductSizeColor.objects.values_list('product_id', flat=True)
    color_ids = ProductSizeColor.objects.values_list('color_id', flat=True)

    products = ProductColorImage.objects.select_related('product', 'color')
    products = products.filter(Q(product_id__in=Subquery(product_ids)) & Q(color_id__in=Subquery(color_ids)))
    return products


def similar_products(product_id, category_id):
    products = products_on_sale().exclude(product__id=product_id)
    products = products.filter(product__category_id=category_id)
    return products


def create_error_404(error_message='Not found'):
    error_data = {'error': error_message}
    return Response(error_data, status=status.HTTP_404_NOT_FOUND)
