from apps.coupon.models import Coupon
from rest_framework import status
from rest_framework.response import Response
from .serializers import CouponSerializer

def validate_coupon(coupon):
    try:
        coupon_obj = Coupon.objects.get(code=coupon)
    except Coupon.DoesNotExist:
        return Response({"message": "Купон не существует"}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({"message": "Купон не доступен"}, status=status.HTTP_403_FORBIDDEN)

    if not coupon_obj.is_available:
        return Response({"message": "Купон не доступен"}, status=status.HTTP_403_FORBIDDEN)

    if coupon_obj.is_expired():
        return Response({"message": "Срок действия истёк"}, status=status.HTTP_403_FORBIDDEN)
    return coupon_obj
