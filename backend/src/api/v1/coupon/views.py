from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.coupon.models import Coupon
from rest_framework import status
from .serializers import *
# from django.db.models import F
from .utils import *

@api_view(['GET'])
def check_coupon(request, coupon):
    result = validate_coupon(coupon)
    if isinstance(result, Response):
        return result
    else:
        response_data =CouponSerializer(result).data
        return Response(response_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def use_coupon(request, coupon):
  pass
