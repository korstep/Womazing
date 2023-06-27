from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.store.models import ProductColorImage, ProductSizeColor, Category
from .serializers import *
from django.db.models import F
from .utils import *
from rest_framework import status


@api_view(['GET'])
def get_products(request, category_slug=None):
    p = get_products_data(category_slug=category_slug,
                          count=request.GET.get('count', None),
                          sort_by=request.GET.get('sort_by', None), )
    if not p.exists():
        return create_error_404('Products not found')
    serializer = GetProductsSerializer(p, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    category = Category.objects.all()
    serializer = GetCategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, product_slug, color_slug):
    p = ProductSizeColor.objects.select_related('product', 'color', 'size')

    pci = products_on_sale()
    colors = p.filter(product__slug=product_slug).distinct('color__id')
    colors = GetColorFromProductSizeColor(colors,many=True).data

    p = p.filter(product__slug=product_slug, color__slug=color_slug)

    if not p.exists():
        return create_error_404('Product not found')

    images = pci.filter(product=p.first().product, color=p.first().color)
    images = GetProductColorImageSerializer(images, many=True).data
    sizes_data = {size['size__size']: size['quantity'] for size in p.values('size__size', 'quantity')}
    firs_element_p = p[0]

    response_data = {
        'name': firs_element_p.product.name,
        'slug': firs_element_p.product.slug,
        'price': firs_element_p.product.price,
        'oldPrice': firs_element_p.product.old_price,
        'selectedColorSlug': firs_element_p.color.slug,
        'images': unpacking_images(images),
        'colors': colors,
        'sizes': sizes_data,
        'similar': GetProductsSerializer(
            similar_products(firs_element_p.product.pk, firs_element_p.product.category.pk), many=True).data
    }
    return Response(response_data)
