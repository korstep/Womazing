from rest_framework import serializers
from apps.store.models import ProductColorImage, ProductSizeColor, Category


class GetProductsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.IntegerField(source='product.price')
    product_old_price = serializers.IntegerField(source='product.old_price')
    color_slug = serializers.CharField(source='color.slug')
    product_slug = serializers.CharField(source='product.slug')
    image = serializers.SerializerMethodField()

    @staticmethod
    def get_image(obj):
        product_image = obj.image.first()  # Assuming image is a related manager
        if product_image:
            return product_image.image.url
        return None

    class Meta:
        model = ProductColorImage
        fields = (
            'product_name',
            'product_price',
            'product_old_price',
            'color_slug',
            'product_slug',
            'image',
        )


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
