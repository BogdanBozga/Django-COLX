from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path("", views.index, name="index"),
    path("home/<int:product_id>/", views.product_detail, name="product"),
    path("user/<int:user_id>/", views.user_detail, name="user"),
    path("home/", views.home, name="home")
]
