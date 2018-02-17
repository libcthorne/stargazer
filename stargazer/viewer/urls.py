from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('repos/', views.repos_show, name='repos_show'),
]
