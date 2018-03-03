from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about')
]