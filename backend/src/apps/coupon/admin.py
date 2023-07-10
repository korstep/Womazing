from .models import *
from django.contrib import admin

# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    list_display = ('id','code','usage_count','is_available','expiry_date')
admin.site.register(Coupon, CouponAdmin)
