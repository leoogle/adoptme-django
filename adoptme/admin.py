from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product, Sale

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Product)
admin.site.register(Sale)