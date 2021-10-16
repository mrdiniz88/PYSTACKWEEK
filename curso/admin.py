from django.contrib import admin
from .models import Aula, Curso, Comentario, NotasAulas

admin.site.register(Curso)
admin.site.register(Aula)
admin.site.register(Comentario)
admin.site.register(NotasAulas)