from django.conf.urls import url
from . import views


urlpatterns = [
      #url(r'^$', views.index, name='index'),
      url(r'ussd',views.ussd_callback, name = 'callback'),
    ]
