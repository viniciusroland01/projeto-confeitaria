from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil',
        verbose_name='Usuário'
    )
    telefone = models.CharField(
        max_length=15,
        default='',
        verbose_name='Telefone',
        help_text='Telefone com WhatsApp (opcional)'
    )
    pontos = models.PositiveIntegerField(
        default=0,
        verbose_name='Pontos de Fidelidade',
        help_text='Pontos acumulados (20 pts = 1 brinde)'
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ['-pontos']

    def __str__(self):
        return f"Perfil de {self.usuario.username} ({self.pontos} pts)"