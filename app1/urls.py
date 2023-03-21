from . import views
from django import urls
from django.urls import path
urlpatterns=[
    path('', views.index, name='api_test_add.html'),
    path('add', views.add, name='api_test_add.html'),
    path('fetch', views.fetch, name='api_test_fetch.html'),
]