from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    def __str__(self):
        return self.name
