import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    phone_number = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='uploads/products/', blank=True)

    def __str__(self):
        return self.name

    def is_recent_product(self):
        return self.added_date >= timezone.now() - datetime.timedelta(days=1)

    @staticmethod
    def get_products_all():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.objects.get(id=product_id)

    @staticmethod
    def get_products_by_location(location):
        return Product.objects.filter(location=location)

    @staticmethod
    def get_products_by_category(category):
        return Product.objects.filter(category=category)

    @staticmethod
    def get_products_by_price(min_price=0, max_price=None):
        if max_price is None:
            return Product.objects.filter(price__gte=min_price)
        return Product.objects.filter(price__gte=min_price, price__lte=max_price)

    @staticmethod
    def get_products_by_name(name):
        return Product.objects.filter(name__icontains=name)

    @staticmethod
    def get_products_filter():
        pass
        # This should be a function that can combine multiple filters
        # and use multiple data about products.

def product_image_path(instance, filename):
    # Images go to products/<product_id>/<filename>
    return f'products/{instance.product.id}/{filename}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)