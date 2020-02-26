from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.destionation_from, name='destinantion_from'),

]