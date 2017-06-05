from django.contrib import admin
from cinema.models import Filme,Sala,Sessao
# Register your models here.
admin.site.register(Sessao)
admin.site.register(Filme)
admin.site.register(Sala)

