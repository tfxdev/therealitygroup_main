from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from others.models import *
from properties.models import *
from properties.filter import *

basic_features = Basic.objects.all()
slider = Slider.objects.all()
blog = Blog.objects.all()
bannerHomeMiddle = bannerHomeMiddle.objects.all()
property_description = property_description.objects.all()


def is_valid_queryparam(param):
    return param != '' and param is not None


def index(request):
    properties = Property.objects.all()
    properties_sosua = properties.filter(location=6)
    properties_cabarete = properties.filter(location=8)
    # Love this property  
    love_id = request.GET.get('love')
    if love_id != None:
        propertytolove = Property.objects.get(pk=love_id)
        user = request.user
        add_love = LovedProperties.objects.create(title=propertytolove, user=user)
        add_love.save()
    lovedProperties = LovedProperties.objects.all().values_list('title_id', flat=True)
    # Love

    return render(request, 'index.html', {
        'basics': basic_features,
        'slider': slider,
        'blogs': blog,
        'bannerHomeMiddle': bannerHomeMiddle,
        'property_description': property_description,
        'properties': properties,
        'lovedProperties': lovedProperties,
        'properties_sosua': properties_sosua,
        'properties_cabarete': properties_cabarete
    })


def Properties_filter(request):
    properties = Property.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    property_count = properties.count()
    page_title = 'Listed properties for sale and rent'

    # Love this property  
    love_id = request.GET.get('love')
    if love_id != None:
        propertytolove = Property.objects.get(pk=love_id)
        user = request.user
        add_love = LovedProperties.objects.create(title=propertytolove, user=user)
        add_love.save()
    lovedProperties = LovedProperties.objects.all().values_list('title_id', flat=True)
    # Love

    grid = request.GET.get('grid')
    
    if grid != None:
        grid_listing = int(request.GET.get('grid'))
    else:
        grid_listing = 12

    grid12 = grid24 = grid48 = 0

    if grid_listing < 13:
        grid12 = 12
        paginator = Paginator(properties, 12)

    elif 20 < grid_listing < 25:
        grid24 = 24
        paginator = Paginator(properties, 24)

    elif grid_listing > 45:
        grid48 = 48
        paginator = Paginator(properties, 48)

    elif not grid != None:
        paginator = Paginator(properties, 12)

    else:
        paginator = Paginator(properties, 12)

    # properties = PropertyFilter(request.GET, queryset=Property.objects.all())
    
    pf = PropertyFilter(request.GET)
    properties = pf.qs

    page_number = request.GET.get('page')

    if page_number is not None:
        properties = paginator.get_page(page_number)
    else:
        properties = paginator.get_page(1)

    context = {

        'basics': basic_features,
        'properties': properties,
        'lovedProperties': lovedProperties,
        'property_count': property_count,
        'pf': pf,
        'grid12': grid12,
        'grid24': grid24,
        'grid48': grid48,
        'page_title': page_title
    }
    return render(request, 'properties.html', context)


def Property_single(request, slug):

    mail_username = request.GET.get('mail_username')
    mail_email_address = request.GET.get('mail_email_address')
    mail_listing_name = request.GET.get('mail_listing_name')
    mail_listing_url = request.GET.get('mail_listing_url')
    mail_listing_id = request.GET.get('mail_listing_id')
    mail_listing_subject = request.GET.get('mail_listing_subject')
    mail_message = request.GET.get('mail_message')

    if mail_listing_url or mail_message or mail_listing_id or mail_listing_name or mail_email_address or mail_username or mail_listing_subject != None:
        print(" Data received" + mail_listing_url + mail_listing_id)

        subject = mail_listing_subject
        message = "Email sent by: " + mail_username + ".<br/> Sender's email address: " + mail_email_address + ".<br/>Email regarding: " + mail_listing_name + ".<br/> Listing url: " + mail_listing_url + ".<br/><hr/> Message from sender: " + mail_message + "<br/><br/>"
        recipint_list = [request.user.email, ]

        send_mail(mail_listing_subject, message, mail_email_address, recipint_list)

    try:
        property = Property.objects.get(slug=slug)
        page_title = property.title
        propertyimage = PropertyImage.objects.filter(property=property)
        meta = property.as_meta()
        return render(request, 'listing-details.html', {
            'basics': basic_features,
            'property': property,
            'propertyimage': propertyimage,
            'meta': meta,
            'page_title':page_title
        })
    except:
        messages.info(request, "Sorry requested post was not found!")


def blogs(request):
    paginator = Paginator(blog, 8)
    page_number = request.GET.get('page')
    blogs_paginated = paginator.get_page(page_number)
    return render(request, 'blog.html', {
        'basics': basic_features,
        'blogs': blogs_paginated,
    })


def blog_single(request, post_id):
    try:
        post = Blog.objects.get(pk=post_id)
        return render(request, 'blog-single.html', {
            'basics': basic_features,
            'blog': post
        })
    except:
        messages.info(request, "Sorry requested post was not found!")


def contact(request):
    return render(request, 'contact.html', {
        'basics': basic_features
    })


def About_page(request): 
    return render(request, 'about.html', {
        'basics': basic_features
    })


def Privacy(request):
    return render(request, 'privacy-policy.html', {
        'basics': basic_features
    })


def Terms(request):
    return render(request, 'terms.html', {
        'basics': basic_features
    })


def Not_found(request, exception=None):
    return render(request, '404.html', {'basics': basic_features})
