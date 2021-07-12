from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.interaction, name='new_interaction')
]
