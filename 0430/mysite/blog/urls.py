from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.article, name='article'),
    url(r'^create/$', views.create, name="create"),
    url(r'^edit/$', views.edit, name="edit"),
]