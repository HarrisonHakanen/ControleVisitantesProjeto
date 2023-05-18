# Generated by Django 4.2.1 on 2023-05-17 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Porteiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('CPF', models.CharField(max_length=11, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone de contato')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='usuarios.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Porteiro',
                'verbose_name_plural': 'Porteiros',
                'db_table': 'porteiros',
            },
        ),
    ]
