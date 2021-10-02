import django_filters
from .models import *


class PropertyFilter(django_filters.FilterSet):
    #price_us = django_filters.NumberFilter()

    price_us__gt = django_filters.NumberFilter(field_name='price_us', lookup_expr='gt')
    price_us__lt = django_filters.NumberFilter(field_name='price_us', lookup_expr='lt')

#    publish_date = django_filters.DateFilter()
#   publish_date__gt = django_filters.DateFilter(field_name='publish_date', lookup_expr='gt')
#   publish_date__lt = django_filters.DateFilter(field_name='publish_date', lookup_expr='lt', )

    class Meta:
        model = Property
        fields = [
            #        			'title',
            # 'featured_image',
            'is_featured',
            #                  'price_us',
            #                  'listing_type',
            'category',
            #                  'property_type',
            'location',
            #                   'lot_Size_m2',
            #                   'lot_Size_ft2',
            #                   'floor_size_m2',
            #                   'floor_size_ft2',
            'floors',
            'beds',
            'baths',
            #                  'property_id',
            'feature',
            # 'short_description',
            # 'details',
            #'publish_date'
        ]
