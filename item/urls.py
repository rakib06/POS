from django.conf.urls import url
from .views import index, display_chair,display_sofa,display_bed
from .views import create_product, edit_chair, delete_chair
urlpatterns =[
    url(r'^$', index, name='index' ),
    url(r'^display_chair', display_chair, name='display_chair'),
    url(r'^display_sofa', display_sofa, name='display_sofa'),
    url(r'^display_bed', display_bed, name='display_bed'),
    url(r'^create_chair', create_product, name='create_chair'),

    url(r'^edit_chair/(?P<pk>\d+)', edit_chair, name='edit_chair'),

url(r'^delete_chair/(?P<pk>\d+)', delete_chair, name='delete_chair')


]