from django.contrib.auth.models import User
from django.db import models
from product.models import Product

class Comment(models.Model):
    title = models.CharField(max_length=80)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
