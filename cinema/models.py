from django.db import models
import datetime

# Create your models here.
# Um modelo diz a Django como trabalhar com os dados que serão armazenados 
# na aplicação.
class Filme(models.Model):
	"""Dados de um filme."""
	name = models.CharField(max_length=200)
	description = models.TextField();
	genre = models.CharField(max_length=50)
	duration = models.CharField(max_length=10);
	# sessao = models.ForeignKey(Sessao,on_delete=models.CASCADE)


	def __str__(self):
		"""Devolve uma representação em string do modelo."""
		return self.name



class Sessao(models.Model):
	"""As sessoas de um filme."""
	time = models.TimeField()
	dataTime = models.DateField()
	filme = models.ForeignKey(Filme,on_delete=models.CASCADE)
	# sala = models.ForeignKey(Sala,on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Sessões"



	def __str__(self):
		strTime = self.time.strftime("%H:%M")
		return strTime

class Sala(models.Model):
	"""A sala da sessao."""
	name = models.CharField(max_length=10)
	filme = models.ForeignKey(Filme,on_delete=models.CASCADE)
	sessao = models.ForeignKey(Sessao,on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Salas"

	def __str__(self):
		return self.name




class Cliente(models.Model):
	"""Representa um cliente: com seus dados,filmes,sessao,sala,cadeira."""