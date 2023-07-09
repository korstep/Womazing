from rest_framework import serializers
from apps.store.models import ProductColorImage, ProductSizeColor, Category, ProductImage


class GetProductsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='product.name')
    productSlug = serializers.CharField(source='product.slug')
    categoryName = serializers.CharField(source='product.category.name')
    categorySlug = serializers.CharField(source='product.category.slug')
    price = serializers.IntegerField(source='product.price')
    oldPrice = serializers.IntegerField(source='product.old_price')
    colorSlug = serializers.CharField(source='color.slug')
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
            'categoryName',
            'categorySlug',
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


class GetProductColorImageSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = ProductColorImage
        fields = ('images',)

    def get_images(self, obj):
        return [image.image.url for image in obj.image.all()]


class GetColorFromProductSizeColor(serializers.ModelSerializer):
    id = serializers.IntegerField(source='color.id')
    name = serializers.CharField(source='color.name')
    slug = serializers.CharField(source='color.slug')
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductSizeColor
        fields = ('id', 'name', 'slug', 'image')

    def get_image(self, obj):
        color_image = obj.color.color_image
        if color_image:
            return color_image.url
        return None


class GetProductOnSizeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='product.name')
    size = serializers.CharField(source='size.size')
    productSlug = serializers.CharField(source='product.slug')
    price = serializers.IntegerField(source='product.price')
    oldPrice = serializers.IntegerField(source='product.old_price')
    color = serializers.CharField(source='color.name')
    colorSlug = serializers.CharField(source='color.slug')
    supply =serializers.IntegerField(source='quantity')

    class Meta:
        model = ProductSizeColor
        fields = (
            'name',
            'size',
            'price',
            'oldPrice',
            'color',
            'colorSlug',
            'productSlug',
            'supply'
        )
