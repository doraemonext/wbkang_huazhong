from django.conf.urls import include, url
from api.views import LoginAPI, BonusHistoryAPI, BonusHistoryDateListAPI, Info1ToNAPI, Calc1ToNAPI, Info1To1API, Calc1To1API

urlpatterns = [
    url(r'^login$', LoginAPI.as_view(), name='login'),
    url(r'^info1ton$', Info1ToNAPI.as_view(), name='info1ton'),
    url(r'^info1to1$', Info1To1API.as_view(), name='info1to1'),
    url(r'^calc1ton$', Calc1ToNAPI.as_view(), name='calc1ton'),
    url(r'^calc1to1$', Calc1To1API.as_view(), name='calc1to1'),
    url(r'^history$', BonusHistoryAPI.as_view(), name='history'),
    url(r'^history_datelist$', BonusHistoryDateListAPI.as_view(), name='history_datelist'),
]
