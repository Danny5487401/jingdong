from django.conf.urls import url

# from .views import RegisterView
from django.urls import re_path

from . import views

app_name = 'users'

urlpatterns = [
    # 用户注册: reverse(users:register) == '/register/'
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    # 判断用户名是否重复注册

]