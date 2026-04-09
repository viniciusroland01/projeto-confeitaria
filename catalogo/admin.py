from django.contrib import admin
from .models import Doce

@admin.register(Doce)
class DoceAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'disponivel')
    list_filter = ('disponivel',)
    search_fields = ('nome',)