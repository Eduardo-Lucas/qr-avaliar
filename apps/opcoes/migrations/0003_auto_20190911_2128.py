# Generated by Django 2.2.5 on 2019-09-12 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcoes', '0002_auto_20190911_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcao',
            name='texto_da_opcao',
            field=models.CharField(max_length=200),
        ),
    ]
