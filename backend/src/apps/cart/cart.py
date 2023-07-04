from decimal import Decimal
from django.conf import settings
from ..store.models import Product, ProductSizeColor, ProductColorImage
from django.utils import timezone
from django.core.exceptions import ValidationError


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.update_supply()

    def get_cart(self):
        return self.cart
    def update_supply(self):
        print(self.cart)
        if len(self.cart) != 0:
            for data in self.cart.values():
                matching_products = ProductSizeColor.objects.get(
                    product__name=data['name'],
                    color__name=data['color'],
                    size__size=data['size']
                )
                data['supply'] = int(matching_products.quantity)

    def __iter__(self):
        """
        Итерация по корзине
        """
        for key in self.cart:
            yield self.cart[key]

    def __len__(self):
        return len(self.cart)

    def add(self, product_id, color_id, size_name, quantity=1):
        if quantity < 1:
            raise ValueError('Количество добавляемых товаров в корзину не может быть меньше 1')
        quantity = int(quantity)
        key = '_'.join([str(x) for x in (product_id, color_id, size_name)])
        cart_item = self.cart.get(key)

        if cart_item:
            matching_products = ProductSizeColor.objects.get(
                product_id=product_id,
                color_id=color_id,
                size__size=size_name
            )
            supply = matching_products.quantity
            if cart_item['quantity_ordered'] + quantity > supply:
                raise ValueError(
                    f"Максимальное количество данного товара в корзине: {supply}")
            else:
                cart_item['quantity_ordered'] += quantity
        else:
            matching_products = ProductSizeColor.objects.get(
                product_id=product_id,
                color_id=color_id,
                size__size=size_name
            )
            matching_images = ProductColorImage.objects.filter(
                product_id=product_id,
                color_id=color_id
            ).first()
            product_image = None
            if matching_images:
                product_image = matching_images.image.first()

            if product_image:
                product_image = product_image.image.url

            supply = int(matching_products.quantity)
            self.cart[key] = {
                'productId': matching_products.product.id,
                'colorId': matching_products.color.id,
                'name': matching_products.product.name,
                'color': matching_products.color.name,
                'size': matching_products.size.size,
                'price': matching_products.product.price,
                'quantityOrdered': 1,
                'supply': supply,
                'image': product_image
            }

        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, key):
        del self.cart[key]
        self.save()

    def reduce(self, key):
        cart_item = self.cart.get(str(key))
        if cart_item:
            if cart_item['quantity_ordered'] == 1:
                raise ValueError(' == 1')
            cart_item['quantity_ordered'] -= 1
        else:
            raise ValueError('Товар не найден')
        self.save()

    def get_total_price(self):
        return sum(int(Decimal(item['price']) * item['quantity_ordered']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
