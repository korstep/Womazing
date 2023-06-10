from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.store.models import ProductColorImage, ProductSizeColor, Category
from .serializers import GetProductsSerializer, GetCategorySerializer
from django.db.models import F
from .utils import get_products_data, products_on_sale, similar_products
from rest_framework import status

# ! Сделать urls в api  v1, v2
# ! Реализовать сортировку в products

# было бы не плохо стандартизировать ошибки или возможно какие-то тесты.
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


# разрезать этот ужас я читаймые части
@api_view(['GET'])
def get_product(request, product_slug, color_slug):
    p = ProductSizeColor.objects.select_related('product', 'color', 'size')

    pci = products_on_sale()
    colors = p.filter(product__slug=product_slug).values(name=F('color__name'),
                                                         slug=F('color__slug'),
                                                         imageUrl=F('color__color_image')).distinct('color__id')

    p = p.filter(product__slug=product_slug, color__slug=color_slug)

    if not p.exists():
        error_data = {'error': 'Product not found'}
        return Response(error_data, status=status.HTTP_404_NOT_FOUND)

    images = pci.filter(product=p.first().product, color=p.first().color).values_list('image__image', flat=True)
    sizes_data = {size['size__size']: size['quantity'] for size in p.values('size__size', 'quantity')}
    firs_element_p = p[0]

    response_data = {
        'name': firs_element_p.product.name,
        'slug': firs_element_p.product.slug,
        'price': firs_element_p.product.price,
        'oldPrice': firs_element_p.product.old_price,
        'selectedColor': firs_element_p.color.slug,
        'colors': colors,
        'images': images,
        'sizes': sizes_data,
        'similar': GetProductsSerializer(
            similar_products(firs_element_p.product.pk, firs_element_p.product.category.pk), many=True).data
    }
    return Response(response_data)
