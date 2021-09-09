from django.urls import path
from .views import inicio, registro, loginView, logoutVista,HomeUser,jugar, resultado_pregunta,tablero

urlpatterns = [
    path('', inicio, name='inicio'),
    path('HomeUser/', HomeUser, name='HomeUser'),
    path('login/', loginView, name='login'),
    path('logout_vista/', logoutVista, name='logout_vista'),
    path('registro/', registro, name='registro'),
    path('tablero/', tablero, name='tablero'),
    path('jugar/', jugar, name='jugar'),
    path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='result'),
]
