from django.shortcuts import render
from .models import Filme,Sessao

# Create your views here.
# Recebe informações de uma requisição ,prepara os dados necessários 
# para gerar uma página e então envia dados de volta ao navegador

def index(request):
	"""A pagina inicial de Cinema"""
	return render(request,'cinema/index.html')

def filmes(request):
	"""Mostra todos os filmes."""
	filmes = Filme.objects.order_by('name')
	# sessao = Sessao.objects.all()
	sessao = {}
	
	for filme in filmes:
		list_sessao = []
		strTime = ""
		sessoes = Sessao.objects.filter(filme__id=filme.id)
		for s in sessoes:
			strTime = s.time.strftime("%H:%M")
			list_sessao.append(strTime)
		sessao[filme.id] = list_sessao


	context = {'filmes' : filmes,'sessao' : sessao}
	return render(request,'cinema/filmes.html',context)



