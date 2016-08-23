from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^main/$', views.index),
    url(r'^registration$', views.user),
    url(r'^login$', views.login),
    url(r'^appointments$', views.success),
    url(r'^logout$', views.logout),
]