from django.conf.urls import include, url
from api.views import LoginAPI

urlpatterns = [
    url(r'^login$', LoginAPI.as_view()),
]
