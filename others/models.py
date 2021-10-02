from django.db import models
from django.db.models import CharField


class Testimonial_Section(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    background = models.ImageField(upload_to='site_pic')


class Testimonials(models.Model):
    rating = models.CharField(max_length=50)
    description = models.TextField()
    client_name = models.CharField(max_length=50)
    client_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='others')


class bannerHomeMiddle(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField()
    button_text = models.CharField(max_length=20)
    button_link = models.CharField(max_length=30)


class property_description(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    featured_text = models.CharField(max_length=20)
