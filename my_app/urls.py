from . import views 
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_search', views.new_search, name='new_search')
]