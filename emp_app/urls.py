from django.conf.urls import url
from . import views


urlpatterns = [
    # /emp/
    url(r'^$', views.index, name='index'),
    url(r'^emp$', views.employee, name='employee'),
]