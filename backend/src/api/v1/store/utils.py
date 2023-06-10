from apps.store.models import ProductColorImage, ProductSizeColor
from django.db.models import Subquery
from django.db.models import Q


def get_products_data(category_slug=None, count=None):
    products = products_on_sale()
    if category_slug:
        products = products.filter(product__category__slug=category_slug)
    if count:
        products = products.order_by('-product_id').distinct('product_id')[:int(count)]
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
