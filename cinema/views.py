from django.shortcuts import render

# Create your views here.
# Um modelo diz a Django como trabalhar com os dados que serão armazenados 
# na aplicação.

class Filme(models.Model):
	"""Dados de um filme."""
	name = models.CharField(max_lenght=200)
	description = models.TextField();
	genre = models.CharField(max_lenght=50)
	duration = models.CharField(max_lenght=10);

	def __str__(self):
		"""Devolve uma representação em string do modelo."""
		return self.name;

class Sessao(models.Model):
	"""As sessoas de um filme."""

class Sala(models.Model):
	"""A sala da sessao."""

class Cliente(models.Model):
	"""Representa um cliente: com seus dados,filmes,sessao,sala,cadeira."""


