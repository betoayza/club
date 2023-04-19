from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('subscribers/', views.subscribers, name='subscribers'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]
