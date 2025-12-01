from django.db import models


class Cargos(models.Model):
    id_empresa = models.ForeignKey('empresas', models.DO_NOTHING, db_column='id_empresa')
    cargo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargos'


class Empresas(models.Model):
    id_endereco = models.ForeignKey('users.Enderecos', models.DO_NOTHING, db_column='id_endereco')
    id_responsavel = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    cnpj = models.CharField(db_column='CNPJ', max_length=50, blank=True, null=True)
    situacao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empresas'


class Status(models.Model):
    nome = models.CharField(max_length=50)
    situacao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'status'

