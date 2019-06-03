from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'basicapp'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
