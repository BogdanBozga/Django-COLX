from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    phone_number = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='products/', blank=True)
    def __str__(self):
        return self.title

def product_image_path(instance, filename):
    # Images go to products/<product_id>/<filename>
    return f'products/{instance.product.id}/{filename}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)