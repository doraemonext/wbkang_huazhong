from django.conf.urls import include, url
from wechat.views import LoginView, MainSelectorView, CalcSelectorView, Calc1ToNView, Calc1To1View, CalcNTo1View, HistoryView

urlpatterns = [
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^main_selector$', MainSelectorView.as_view(), name='main_selector'),
    url(r'^calc_selector$', CalcSelectorView.as_view(), name='calc_selector'),
    url(r'^calc_1ton$', Calc1ToNView.as_view(), name='calc_1ton'),
    url(r'^calc_1to1$', Calc1To1View.as_view(), name='calc_1to1'),
    url(r'^calc_nto1$', CalcNTo1View.as_view(), name='calc_nto1'),
    url(r'^history$', HistoryView.as_view(), name='history'),
]
