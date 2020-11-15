from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path

from sosmed import views

urlpatterns = [
    url(r'sosmed/delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    url(r'sosmed/update/(?P<update_id>[0-9]+)$', views.update, name='update'),
    path('sosmed/create', views.create , name='create'),
    path('sosmed/list', views.list , name='list'),
    path('admin/', admin.site.urls),
]
