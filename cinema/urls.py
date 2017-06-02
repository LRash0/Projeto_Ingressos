"""Define padrões de URL para learning_logs"""

from django.conf.urls import url

from . import views

urlpatterns = [
	# Pagina inicial
	url(r'^$', views.index,name='index'),
]