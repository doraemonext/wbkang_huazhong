from django.conf.urls import include, url
from wechat.views import LoginView, MainSelectorView

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^main_selector$', MainSelectorView.as_view()),
]
