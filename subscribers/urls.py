from django.urls import path
from . import views

urlpatterns = [
    path('subscribers/', views.subscribers, name='subscribers')
]