# Generated by Django 2.2.5 on 2019-09-08 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_da_pergunta', models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Pergunta',
                'verbose_name_plural': 'Perguntas',
                'ordering': ['texto_da_pergunta'],
            },
        ),
    ]
