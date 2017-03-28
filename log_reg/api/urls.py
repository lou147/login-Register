from django.conf.urls import url
from .views import register, user_login, login_or_not


urlpatterns = [
    url(r'^api/register/$', register),
    url(r'^api/login/$', user_login),
    url(r'^api/login_or_not/$', login_or_not),
]

