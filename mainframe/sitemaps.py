from django.contrib.sitemaps import Sitemap

from properties.models import *

class Propertysitemap(Sitemap):
	changefreq = "Weekly"
	priority = 0.9

	def items(self):
		return Property.objects.all()

	def lastmod(self, obj):
		return obj.publish_date