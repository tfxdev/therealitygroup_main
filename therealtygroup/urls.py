from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from mainframe.sitemaps import *

sitemaps = {
    "posts" : Propertysitemap,
} 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainframe.urls')),
    path('tinymce/', include('tinymce.urls')),  
    path('user/', include('user.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.view.sitemap')
]

handler404 = 'mainframe.views.Not_found'

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
