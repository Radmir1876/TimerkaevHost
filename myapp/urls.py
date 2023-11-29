from django.contrib import admin
from django.urls import path, re_path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('error/', views.error, name='error'),
    re_path(r'^user/(?:(?P<login>[\w]+)/(?P<folder>[\w]+)/(?P<number>\d+)/)?$', views.user, name='user'),
]
