from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import login , logout
from django.contrib.auth import views as auth_views


app_name = 'userdata'
urlpatterns= [
    url(r'^$' , views.home , name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$' , views.register , name = 'register'),
    url(r'^(?P<slug>[-\w]+)/$' , views.profile , name = 'profile'),
    url(r'^(?P<slug>[-\w]+)/edit$' , views.edit_profile , name = 'edit_profile'),

    url(r'^(?P<slug>[-\w]+)/change_password$' , views.change_password , name = 'change_password'),

]
