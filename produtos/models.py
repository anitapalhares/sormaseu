from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=69)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome

# Create your models here.
