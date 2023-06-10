from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.store.models import ProductColorImage, ProductSizeColor, Category
from .serializers import GetProductsSerializer, GetCategorySerializer
from django.db.models import F
from django.db.models import OuterRef, Exists
from .utils import get_products_data
from rest_framework import status


@api_view(['GET'])
def get_products(request, category_slug=None):
    p = get_products_data(category_slug=category_slug,
                          count=request.GET.get('count', None))
    if not p.exists():
        error_data = {'error': 'Products not found'}
        return Response(error_data, status=status.HTTP_404_NOT_FOUND)
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
    pci = ProductColorImage.objects.select_related('product', 'color')
    product_size_color_exists = Exists(p.filter(
        product=OuterRef('product'),
        color=OuterRef('color')
    ))
    pci = pci.filter(product_size_color_exists)
    colors = p.filter(product__slug=product_slug).values(name=F('color__name'),
                                                         slug=F('color__slug'),
                                                         imageUrl=F('color__color_image')).distinct('color__id')

    p = p.filter(product__slug=product_slug, color__slug=color_slug)

    if not p.exists():
        error_data = {'error': 'Product not found'}
        return Response(error_data, status=status.HTTP_404_NOT_FOUND)

    matching_images = pci.filter(product=p.first().product, color=p.first().color).annotate(
        imageUrl=F('image__image')
    ).values('imageUrl')
    matching_images = matching_images.values_list('imageUrl', flat=True)
    images = list(matching_images)
    sizes = p.values('size__size', 'quantity')
    sizes_data = {size['size__size']: size['quantity'] for size in sizes}
    firs_element_p = p[0]

    response_data = {
        'name': firs_element_p.product.name,
        'price': firs_element_p.product.price,
        'oldPrice': firs_element_p.product.old_price,
        'selectedColor': firs_element_p.color.pk,
        'colors': colors,
        'images': images,
        'sizes': sizes_data,
    }
    return Response(response_data)
