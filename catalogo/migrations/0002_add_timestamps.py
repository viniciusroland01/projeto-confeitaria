# Generated migration - adds new fields and updates verbose names

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doce',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='doce',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='doce',
            name='nome',
            field=models.CharField(help_text='Nome do produto', max_length=100, verbose_name='Nome do Doce'),
        ),
        migrations.AlterField(
            model_name='doce',
            name='preco',
            field=models.DecimalField(decimal_places=2, help_text='Preço em reais (R$)', max_digits=7, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='doce',
            name='imagem',
            field=models.ImageField(help_text='Foto do produto', upload_to='doces/', verbose_name='Imagem do Doce'),
        ),
        migrations.AlterField(
            model_name='doce',
            name='disponivel',
            field=models.BooleanField(default=True, help_text='Marque se o produto está disponível', verbose_name='Disponível'),
        ),
    ]
