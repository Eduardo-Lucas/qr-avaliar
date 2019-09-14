# Generated by Django 2.2.5 on 2019-09-14 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_inicio', models.DateTimeField(verbose_name='Data de Início')),
                ('data_termino', models.DateTimeField(verbose_name='Data de Término')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição do Evento')),
                ('publico_privado', models.CharField(choices=[('PUBLICO', 'Público'), ('PRIVADO', 'Privado')], default='PUBLICO', max_length=2)),
                ('local', models.CharField(max_length=100)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('bairro', models.CharField(blank=True, max_length=25, null=True)),
                ('cidade', models.CharField(blank=True, max_length=25, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
                ('absorver_taxa_servico', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresa')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'unique_together': {('empresa', 'nome', 'data_inicio')},
            },
        ),
    ]
