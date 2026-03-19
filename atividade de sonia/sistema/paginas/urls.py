from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('sobre/', views.sobre),
    path('projetos/', views.projetos),
    path('contato/', views.contato),
]