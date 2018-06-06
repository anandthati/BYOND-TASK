from django.conf import settings
from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import logout, login
from django.contrib.auth import views as auth_views
regex = '[\w!@#$%^&*()+,.;:\'"-_ ]' #pylint: disable=anomalous-backslash-in-string
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name':'index.html'}, name='logout'),
    url(r'^singup$', views.register, name='signupform'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^writepost$', views.writepost, name='writepost'),
    url(r'^readpost/(?P<pk>\d+)/$', views.readpost, name='readpost'),

    url(r'^',include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    
    ]
