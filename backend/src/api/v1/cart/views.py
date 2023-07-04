from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.cart.cart import Cart
from .utils import *


@api_view(['GET'])
def get_cart(request):
    cart = Cart(request)
    return Response(cart.get_cart())


@api_view(['PUT'])
def add_product(request):
    product_id = request.query_params.get('product_id')
    color_id = request.query_params.get('color_id')
    size = request.query_params.get('size')
    if not (product_id and color_id and size):
        error_message = 'No parameters are required'
        return Response({'error': error_message}, status=400, content_type='application/json')

    cart = Cart(request)
    try:
        cart.add(product_id=product_id, color_id=color_id, size_name=size)
        return Response({'success': 'Product added successfully'}, status=200, content_type='application/json')
    except ValueError as e:
        error_message = str(e)
        return Response({'error': error_message}, status=400, content_type='application/json')
    except Exception as e:
        error_message = 'An error occurred while adding the product'
        return Response({'error': error_message}, status=500, content_type='application/json')
