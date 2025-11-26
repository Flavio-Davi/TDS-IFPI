from django.contrib import admin
from website.models import Tutor, Animal, Relato


class TutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'lista_especie_animais_tutor')
    ordering = ('-nome',)
    search_fields = ('nome',)


class AnimalAdmin(admin.ModelAdmin):
    list_filter = ('especie', 'raca')


class RelatoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tutor, TutorAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Relato, RelatoAdmin)
