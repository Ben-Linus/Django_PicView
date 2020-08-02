from django.contrib import admin
from . models import Image, Category
# Register your models here.

admin.site.register(Category)
admin.site.register(Image)