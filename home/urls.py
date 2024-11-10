from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre', views.sobre, name="sobre"),
    path('contato', views.contato, name="contato"),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('diadasemana/<int:dia>/', views.diadasemana, name='diadasemana'),
    path('cadweb/', views.cadweb, name='cadweb'),

]