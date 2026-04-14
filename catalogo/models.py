from django.db import models

class Doce(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome do Doce',
        help_text='Nome do produto'
    )
    preco = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Preço',
        help_text='Preço em reais (R$)'
    )
    imagem = models.ImageField(
        upload_to='doces/',
        verbose_name='Imagem do Doce',
        help_text='Foto do produto'
    )
    disponivel = models.BooleanField(
        default=True,
        verbose_name='Disponível',
        help_text='Marque se o produto está disponível'
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
        verbose_name = 'Doce'
        verbose_name_plural = 'Doces'
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"
