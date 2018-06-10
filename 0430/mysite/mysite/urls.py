from django.conf.urls import url,include
from django.contrib import admin
from mothers_day.views import *
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$', form), 
    url(r'^blog/', include('blog.urls')), 
]
