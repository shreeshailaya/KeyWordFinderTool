from django.contrib import admin
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'appsearcher',include('appsearcher.urls')),
    url(r'keywordfinder',include('keywordfinder.urls')),
    url(r'^about$',views.about),
    url(r'^$',views.homepage),
]
