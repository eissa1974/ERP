from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$' , views.all_notes , name = 'all_notes'),
##    url(r'^(?P<id>\d+)$' , views.detail , name = 'note_detail'),
]
