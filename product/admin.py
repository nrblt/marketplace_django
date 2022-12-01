from django.contrib import admin

from .models import Dislike, Like, Product

admin.site.register(Product)
admin.site.register(Like)
admin.site.register(Dislike)
