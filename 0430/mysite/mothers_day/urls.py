from django.conf.urls import url

from . import views

app_name = 'mothers_day'
urlpatterns = [
    url(r'^$', views.form, name='form'),
    url('a', views.search, name='search'),
]
