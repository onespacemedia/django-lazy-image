from django.urls import re_path

from .views import ImageView, OSMImageRefFieldImageView

urlpatterns = [
    re_path(
        r'thumbnail/'
        r'(?P<name>[a-zA-Z0-9-_.]+)/'
        r'(?P<model>\w+\.\w+)/'
        r'(?P<pk>\d+)/'
        r'(?P<field>\w+)/'
        r'(?P<width>\d+|auto)/'
        r'(?P<height>\d+|auto)/'
        r'(?P<format>source|jpg|png|webp)/'
        r'(?P<crop>[^/]+)/'
        r'(?P<quality>\d+|60)/',
        ImageView.as_view(),
        name='thumbnail'
    ),
    re_path(
        r'thumbnail/'
        r'(?P<pk>\d+)/'
        r'(?P<width>\d+|auto)/'
        r'(?P<height>\d+|auto)/'
        r'(?P<format>source|jpg|png|webp)/'
        r'(?P<crop>[^/]+)/'
        r'(?P<quality>\d+|60)/',
        OSMImageRefFieldImageView.as_view(),
        name='osm_thumbnail'
    ),
]
