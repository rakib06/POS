from django.conf.urls import url
from .views import index, display_item,create_item
#from .views import create_item, edit_chair, delete_chair

urlpatterns =[
    url(r'^$', index, name='index' ),
    url(r'^display_item', display_item, name='display_item'),
    url(r'^create_item', create_item, name='create_item'),


]

'''
url(r'^display_sofa', display_sofa, name='display_sofa'),
    url(r'^display_bed', display_bed, name='display_bed'),
    url(r'^create_chair', create_product, name='create_chair'),

    url(r'^edit_chair/(?P<pk>\d+)', edit_chair, name='edit_chair'),

url(r'^delete_chair/(?P<pk>\d+)', delete_chair, name='delete_chair')
'''