from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

from datetime import datetime
import uuid
import os

# Create your models here.



def rename_image(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    
    if hasattr(instance, 'judul') and instance.judul:
        filename = f"{slugify(instance.judul)}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    elif hasattr(instance, 'title') and instance.title:
        filename = f"{slugify(instance.title)}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    elif instance.pk:
        filename = f"{instance.pk}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    else:
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    
    return os.path.join(upload_to, filename)

class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_siswa = models.BooleanField('Is siswa', default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Stats(models.Model):
    students = models.CharField(max_length=20)
    teachers = models.CharField(max_length=20)
    staffs = models.CharField(max_length=20)
    registrations = models.CharField(max_length=20)

    def __str__(self):
        return "Stats"

    class Meta:
        verbose_name_plural = "Stats"

class PostNews(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='post_images/', null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title

@receiver(pre_save, sender=PostNews)
def pre_save_postnews_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

class Media (models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='media_images/', null=True, blank=True)
    content = models.TextField()
    url_drive = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to=rename_image, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title
    
class Program(models.Model):
    title = models.CharField(max_length=100)
    penanggung_jawab = models.CharField(max_length=100)
    images = models.ImageField(upload_to='program_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title
    

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    ISBN = models.CharField(max_length=200, unique=True)
    berat = models.DecimalField(max_digits=5, decimal_places=2)
    sinopsis = models.TextField()
    images = models.ImageField(upload_to=rename_image, null=True, blank=True)

    def __str__(self):
        return self.judul