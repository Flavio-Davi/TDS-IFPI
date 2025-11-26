from django.db import models

class Tutor(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    endereco = models.TextField()


    def __str__(self):
        return self.nome


    def lista_especie_animais_tutor(self):
        lista = [c.especie for c in self.animais.all()]
        return lista
    lista_especie_animais_tutor.short_description = 'Minhas Espécies'
    
class Animal(models.Model):
    nome = models.CharField(max_length=200)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='animais')

    def __str__(self):
        return self.nome


class Relato(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    relato = models.TextField()
    diagnostico = models.CharField(max_length=200)
    recomendacao = models.TextField()

