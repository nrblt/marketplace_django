from django.db import models
from PIL import Image
from tasks import resize_image

class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/')
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save()
        resize_image(self.image)
