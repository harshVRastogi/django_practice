from django.conf.urls import url
from . import views

urlpatterns = [
    # /myfirstapp/
    url(r'^$', views.index, name="index"),
    # /details/id/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name="details"),
]
