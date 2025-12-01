from django.contrib import admin
from .models import ChatParticipantes, Chats, Mensagens


admin.site.register(ChatParticipantes)
admin.site.register(Chats)
admin.site.register(Mensagens)
