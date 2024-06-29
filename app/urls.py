from django.contrib import admin
from django.urls import path

from app.views import index_page, product_detail_page

urlpatterns = [
    path('', index_page, name='index'),
    path('product/', product_detail_page, name='product_detail'),
]