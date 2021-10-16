from django.urls import __path__
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curso/<int:id>', views.curso, name='curso'),
    path('aula/<int:id>', views.aula, name = 'aula'),
    path('comentarios/', views.comentarios, name = 'comentarios'),
    path('processa_avaliacao/', views.processa_avaliacao, name = 'processa_avaliacao')
]