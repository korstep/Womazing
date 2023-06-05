from apps.store.models import ProductColorImage, ProductSizeColor
from django.db.models import Subquery
from django.db.models import Q


def get_products_data(category_slug=None, count=None):
    product_ids = ProductSizeColor.objects.values_list('product_id', flat=True)
    color_ids = ProductSizeColor.objects.values_list('color_id', flat=True)

    p = ProductColorImage.objects.select_related('product', 'color')
    p = p.filter(Q(product_id__in=Subquery(product_ids)) & Q(color_id__in=Subquery(color_ids)))
    if category_slug:
        p = p.filter(product__category__slug=category_slug)
    if count:
        p = p.order_by('-product_id').distinct('product_id')[:int(count)]
    return p
