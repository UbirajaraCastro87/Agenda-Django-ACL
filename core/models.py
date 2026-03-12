from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Eventos(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateField()
    data_criacao = models.DateField(auto_now =True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos'

    def __str__(self):
        return self.titulo

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M')
