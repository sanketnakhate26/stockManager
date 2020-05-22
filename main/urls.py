from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.overview, name='overview'),
    url('^add/', views.addstock, name='addstock'),
]