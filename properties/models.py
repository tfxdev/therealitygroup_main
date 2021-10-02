from django.db import models
from tinymce.models import HTMLField
from django.conf import settings
from meta.models import ModelMeta
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Floors(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Beds(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Baths(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Property_features(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Property(ModelMeta, models.Model):
    featured_image = models.ImageField(upload_to='p_images', default=None, blank=True)
    is_featured = models.BooleanField(default=False)
    # gallery_images = models.FileField(blank=True)
    title = models.CharField(max_length=250)
    price_us = models.IntegerField(default=None, blank=True, null=True)
    listing_type = models.CharField(max_length=250, blank=True, default=None, null=True)
    category = models.ManyToManyField(Category, default=None, null=True)
    property_type = models.CharField(max_length=20, default=None, blank=True, null=True)
    location = models.ManyToManyField(Location, blank=True, default=None)
    lot_Size_m2 = models.IntegerField(default=None, blank=True, null=True)
    lot_Size_ft2 = models.IntegerField(default=None, blank=True, null=True)
    floor_size_m2 = models.IntegerField(default=None, blank=True, null=True)
    floor_size_ft2 = models.IntegerField(default=None, blank=True, null=True)
    floors = models.ManyToManyField(Floors, blank=True, default=None)
    beds = models.ManyToManyField(Beds, blank=True, default=None)
    baths = models.ManyToManyField(Baths, blank=True, default=None)
    property_id = models.CharField(max_length=30, blank=True, default=None, null=True)
    feature = models.ManyToManyField(Property_features, related_name='Features', default=None)
    short_description = models.TextField(max_length=1500, default=None, help_text='For under title description and SEO')
    details = HTMLField(blank=True, default=None, null=True)
    publish_date = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateField(default=None ,null=True)
    slug = AutoSlugField(populate_from='title', null=True, default=None, unique=True)
    seo_title = models.CharField(null=True, blank=True, default=None, max_length=60)
    seo_description = models.TextField(null=True, blank=True, default=None, max_length=150)





    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/property/%i/" % self.id

    def get_meta_image(self):
        if self.featured_image:
            return self.featured_image.url

    _metadata = {
        'title' : 'title',
        'description' : 'short_description',
        "og_title": 'title',
        "twitter_title": 'title',
        "schemaorg_title": 'title',
        "og_description": 'short_description',
        "twitter_description": 'short_description',
        "schemaorg_description": 'short_description',
        "keywords": False,
        "published_time": 'publish_date',
        "modified_time": False,
        "expiration_time": False,
        "tag": 'category',
        "url": False,
        "locale": False,
    }



class PropertyImage(models.Model):
    property = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='property_images')

    def __str__(self):
        return self.property.title


class LovedProperties(models.Model):
    title = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lovedate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property.title
