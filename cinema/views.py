from django.shortcuts import render
from .models import Filme,Sala,Sessao

# Create your views here.
# Recebe informações de uma requisição ,prepara os dados necessários 
# para gerar uma página e então envia dados de volta ao navegador

def index(request):
	"""A pagina inicial de Cinema"""
	return render(request,'cinema/index.html')

def filmes(request):
	"""Mostra todos os filmes."""
	filmes = Filme.objects.order_by('name')
	sessao = Sessao.objects.all()
	salas = Sala.objects.all()
	context = {"filmes" : filmes, "sessao" : sessao, "salas" : salas}
	return render(request,'cinema/filmes.html',context)



