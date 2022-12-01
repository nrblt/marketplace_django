from brand.models import Brand
from category.models import Category
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    GENDER_CHOICE = (
        ("male","male"),
        ("female","female"),
        ("unisex","unisex"),
    )
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = ArrayField(models.CharField(max_length=150))
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type = models.CharField(max_length=150)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=150)
    price = models.IntegerField()
    count = models.IntegerField()
    material = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    color = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.brand.name} - {self.name} "

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Like)
def liked(sender, instance, created, **kwargs):
    if created:
        instance.product.likes += 1
        instance.product.save()


@receiver(post_save, sender=Dislike)
def disliked(sender, instance, created, **kwargs):
    if created:
        instance.product.dislikes += 1
        instance.product.save()
