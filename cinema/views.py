from django.shortcuts import render
from .models import Filmes

# Create your views here.
# Recebe informações de uma requisição ,prepara os dados necessários 
# para gerar uma página e então envia dados de volta ao navegador

def index(request):
	"""A pagina inicial de Cinema"""
	return render(request,'cinema/index.html')

def filmes(request):
	"""Mostra todos os filmes."""
	filmes = 



