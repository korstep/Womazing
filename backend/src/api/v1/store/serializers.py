from rest_framework import serializers
from apps.store.models import ProductColorImage, ProductSizeColor, Category


class GetProductsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='product.name')
    price = serializers.IntegerField(source='product.price')
    old_price = serializers.IntegerField(source='product.old_price')
    color_slug = serializers.CharField(source='color.slug')
    product_slug = serializers.CharField(source='product.slug')
    image_url = serializers.SerializerMethodField()

    @staticmethod
    def get_image_url(obj):
        product_image = obj.image.first()  # Assuming image is a related manager
        if product_image:
            return product_image.image.url
        return None

    class Meta:
        model = ProductColorImage
        fields = (
            'name',
            'price',
            'old_price',
            'color_slug',
            'product_slug',
            'image_url',
        )


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
