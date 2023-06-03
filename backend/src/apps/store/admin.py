from .models import *
from django.utils.text import slugify
from unidecode import unidecode
from django.contrib import admin


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'old_price', 'category')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.slug = slugify(f"{obj.id}-{unidecode(obj.name)}")
        super().save_model(request, obj, form, change)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')


class ProductSizeColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size', 'quantity')
    list_filter = ('product', 'color', 'size', 'quantity')
    search_fields = ('product__name',)

    # def get_images(self, obj):
    #     images = obj.image_url.all()
    #     return [image.image.url for image in images]


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


class ProductColorImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color')


admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ProductSizeColor, ProductSizeColorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductColorImage, ProductColorImageAdmin)