from django.contrib import admin
from .models import Perfil
from django.contrib import messages

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone', 'pontos', 'status_recompensa')
    search_fields = ('usuario__username', 'telefone')
    list_filter = ('pontos',)

    # Função para a Fernanda ver rápido quem ganhou brinde
    def status_recompensa(self, obj):
        if obj.pontos >= 20:
            return "🎁 GANHOU RECOMPENSA!"
        return "Em andamento"

    # Ação Manual: Fernanda seleciona o cliente e clica em "Confirmar Pontos"
    actions = ['adicionar_pontos_compra', 'resgatar_recompensa']

    def adicionar_pontos_compra(self, request, queryset):
        for perfil in queryset:
            # Aqui você pode definir um valor padrão ou perguntar. 
            # Para simplificar, vamos somar +2 pontos por confirmação manual:
            perfil.pontos += 2 
            perfil.save()
            self.message_user(request, f"Pontos adicionados para {perfil.usuario.username}. Saldo: {perfil.pontos}")
    
    adicionar_pontos_compra.short_description = "Confirmar Pedido: +2 pontos"

    def resgatar_recompensa(self, request, queryset):
        for perfil in queryset:
            if perfil.pontos >= 20:
                perfil.pontos -= 20
                perfil.save()
                self.message_user(request, f"Recompensa resgatada para {perfil.usuario.username}!")
            else:
                self.message_user(request, f"{perfil.usuario.username} ainda não tem 20 pontos.", messages.ERROR)
    
    resgatar_recompensa.short_description = "Usar Recompensa (Gasta 20 pts)"