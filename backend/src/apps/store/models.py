from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    old_price = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.id}-{unidecode(self.name)}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Color(models.Model):
    color_image = models.ImageField(upload_to='color_images/', null=True, default=None)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=255)

    def __str__(self):
        return self.size


class ProductSizeColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, default=None, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, default=None, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.product} - {self.color} - {self.size}"


class ProductColorImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, default=None, on_delete=models.SET_DEFAULT)
    image = models.ManyToManyField("ProductImage")


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.image.url
