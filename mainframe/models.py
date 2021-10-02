from django.db import models
from tinymce.models import HTMLField


class Basic(models.Model):
    site_title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='site_pic')
    favicon = models.ImageField(upload_to='site_pic')
    logo_link = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    phone_link = models.CharField(max_length=50)
    email = models.CharField(max_length=35)
    email_link = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    facebook_link = models.CharField(max_length=50)
    twitter_link = models.CharField(max_length=50)
    footer_background = models.ImageField(upload_to='site_pic')
    footer_logo = models.ImageField(upload_to='site_pic')
    footer_description = models.TextField()
    footer_about_title = models.CharField(max_length=50)
    footer_about = models.CharField(max_length=50)
    footer_contact_description = models.CharField(max_length=250)
    copyright_text = models.CharField(max_length=250)


class Slider(models.Model):
    background_image = models.ImageField(upload_to='slider_images')
    title_top = models.CharField(max_length=220, null=True)
    title = models.CharField(max_length=300, null=True)
    description = models.TextField(null=True)
    button_text = models.CharField(max_length=50, null=True)
    button_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=220)
    image = models.ImageField(upload_to='blog_images')
    short_description = models.TextField(max_length=250)
    description = HTMLField(null=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
