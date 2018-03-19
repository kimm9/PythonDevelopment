from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('add_category/', views.add_category, name='add_category'),
  path('category/<category_name_slug>/', views.show_category, name='show_category')
]