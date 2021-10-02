from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *
from mainframe.models import *

basic_features = Basic.objects.all()


def Property_single(request, ):
    try:
        property_d = Property.objects.get(pk=1)
        return render(request, 'listing-details.html', {'basics': basic_features,'property': property_d })
    except:
        messages.info(request, "Sorry requested post was not found!")
