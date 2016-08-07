from django.conf.urls import include, url
from wechat.views import LoginView, MainSelectorView, CalcSelectorView, Calc1ToNView

urlpatterns = [
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^main_selector$', MainSelectorView.as_view(), name='main_selector'),
    url(r'^calc_selector$', CalcSelectorView.as_view(), name='calc_selector'),
    url(r'^calc_1ton$', Calc1ToNView.as_view(), name='calc_1ton'),
]
