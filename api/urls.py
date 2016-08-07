from django.conf.urls import include, url
from api.views import LoginAPI, BonusHistoryAPI, BonusHistoryDateListAPI, Info1ToNAPI

urlpatterns = [
    url(r'^login$', LoginAPI.as_view(), name='login'),
    url(r'^info1ton$', Info1ToNAPI.as_view(), name='info1ton'),
    url(r'^history$', BonusHistoryAPI.as_view(), name='history'),
    url(r'^history_datelist$', BonusHistoryDateListAPI.as_view(), name='history_datelist'),
]
