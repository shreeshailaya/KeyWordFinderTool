from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.appsearcher),
    url(r'header',views.header),
    url(r'playstore/$',views.getPlayStoreInfo),
    url(r'iosstore/$',views.getIosStoreInfo),
]

