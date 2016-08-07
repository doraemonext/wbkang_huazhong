from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^wechat/', include('wechat.urls', namespace='wechat')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
]
