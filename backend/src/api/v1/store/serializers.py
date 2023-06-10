from rest_framework import serializers
from apps.store.models import ProductColorImage, ProductSizeColor, Category


class GetProductsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='product.name')
    price = serializers.IntegerField(source='product.price')
    oldPrice = serializers.IntegerField(source='product.old_price')
    colorSlug = serializers.CharField(source='color.slug')
    productSlug = serializers.CharField(source='product.slug')
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
            'name',
            'price',
            'oldPrice',
            'colorSlug',
            'productSlug',
            'image',
        )


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'slug'
            )
