from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from main.views import user_login, user_logout, success


urlpatterns = [
    url('^admin/', admin.site.urls),
    url('', include('main.urls')),
    path('login/',user_login, name="user_login"),
    path('success/',success, name="user_success"),
    path('logout/',user_logout, name="user_logout"),



]
