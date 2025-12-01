from django.db import models


class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    id_endereco = models.ForeignKey('users.Enderecos', on_delete=models.CASCADE)
    id_cargo = models.ForeignKey('setting.Cargos', on_delete=models.CASCADE)
    id_status = models.ForeignKey('setting.Status', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, blank=False)
    senha = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=100, blank=False)
    data_nascimento = models.DateField()
    data_criacao = models.DateTimeField()


    class Meta:
        db_table = 'usuarios'


class Enderecos(models.Model):
    id = models.IntegerField(primary_key=True)
    rua = models.CharField(max_length=50, blank=False)
    bairro = models.CharField(max_length=50, blank=False)
    cidade = models.CharField(max_length=50, blank=False)
    estado = models.CharField(max_length=50, blank=False)


    class Meta:
        db_table = 'enderecos'


class Contatos(models.Model):
    id = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey('users.Usuarios', on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)


    class Meta:
        db_table = 'contatos'
        