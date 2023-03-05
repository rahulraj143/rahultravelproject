from . import views
from django.urls import path

urlpatterns = [

path('regist',views.regist,name='regist'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout')


]