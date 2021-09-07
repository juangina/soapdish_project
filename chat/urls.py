from django.conf.urls import url
from django.contrib import admin
from .views import ChatterBotAppView, ChatterBotApiView


urlpatterns = [
    # url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', ChatterBotAppView.as_view(), name='chat'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]
