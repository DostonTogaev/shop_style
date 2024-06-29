from django.contrib.auth.models import User, Group
from django.contrib import admin

from app.models import Product, Category

# Register your models here.

admin.site.register(Product)




admin.site.unregister(User)
admin.site.unregister(Group)