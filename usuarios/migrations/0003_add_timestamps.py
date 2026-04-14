
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_perfil_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to='auth.user', verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(default='', help_text='Telefone com WhatsApp (opcional)', max_length=15, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='pontos',
            field=models.PositiveIntegerField(default=0, help_text='Pontos acumulados (20 pts = 1 brinde)', verbose_name='Pontos de Fidelidade'),
        ),
    ]
