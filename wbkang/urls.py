from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^wechat/', include('wechat.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
