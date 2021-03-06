# Generated by Django 2.2.5 on 2019-09-20 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perguntas', '0001_initial'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Botão', 'Botão'), ('Texto', 'Texto')], default='Botão', max_length=15)),
                ('ordem', models.PositiveIntegerField(default=1)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perguntas.Pergunta')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
                'ordering': ['ordem'],
                'unique_together': {('evento', 'pergunta')},
            },
        ),
    ]
