from django.db import models


class ChatParticipantes(models.Model):
    id_chat = models.ForeignKey('chat.Chats', models.DO_NOTHING, db_column='id_chat')
    id_usuario = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_usuario')
    papel = models.CharField(max_length=13, blank=True, null=True)
    data_entrada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_participantes'


class Chats(models.Model):
    id_empresa = models.ForeignKey('setting.Empresas', models.DO_NOTHING, db_column='id_empresa')
    nome = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=7, blank=True, null=True)
    situacao = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chats'


class Mensagens(models.Model):
    id_chat = models.ForeignKey(Chats, models.DO_NOTHING, db_column='id_chat')
    id_remetente = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_remetente')
    id_destinatario = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_destinatario', related_name='mensagens_id_destinatario_set')
    mensagem = models.TextField()
    data_envio = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagens'
