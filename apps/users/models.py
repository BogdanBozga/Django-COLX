from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_verified = models.BooleanField(default=False)
    total_sales = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
