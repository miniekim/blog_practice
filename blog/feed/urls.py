from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.detail, name='index'),
    # url(r'^$', views.about, name='index'),
]