from PIL import Image
from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def resize_image(image):
    image1 = Image.open(image.path)
    image1 = image1.resize((300,300), Image.ANTIALIAS)
    image1.save(image.path, quality=95)
