from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.product_detail, name="product"),
    path("<int:user_id>/", views.user_detail, name="user"),
    path("home/", views.home, name="home")
]