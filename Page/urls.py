from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='_Single-page'),
]
