# Generated by Django 2.2.5 on 2019-09-13 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('respostas_padroes', '0002_auto_20190913_1632'),
        ('opcoes', '0005_auto_20190912_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opcao',
            name='texto_da_opcao',
        ),
        migrations.AddField(
            model_name='opcao',
            name='opcao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='respostas_padroes.RespostaPadrao'),
            preserve_default=False,
        ),
    ]