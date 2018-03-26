from django.conf.urls import url
from . import views
from django.urls import include, path


urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('add_category/', views.add_category, name='add_category'),
  path('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
  path('category/<category_name_slug>/', views.show_category, name='show_category'),
  path('register/', views.register, name='register'),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('restricted/', views.restricted, name='restricted'),
  path('search/', views.search, name='search'),
  path('goto/', views.track_url, name='goto'),
  ]



