from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:post_id>', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.About_page, name='about_page'),
    path('privacy/', views.Privacy, name='privacy_page'),
    path('terms/', views.Terms, name='terms_page'),
    path('properties/', views.Properties_filter, name='properties_filter'),
    path('properties?is_featured=unknown&price_us__gt=&price_us__lt=&grid=12', views.Properties_filter, name='properties_filter'),
    path('property/<slug:slug>/', views.Property_single, name="properties_home"),
]
