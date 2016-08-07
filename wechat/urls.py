from django.conf.urls import include, url
from wechat.views import LoginView

urlpatterns = [
    url(r'^$', LoginView.as_view()),
]
