# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOfficina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(verbose_name='Nome', max_length=30),
        ),
        migrations.AlterField(
            model_name='client',
            name='nickname',
            field=models.CharField(verbose_name='Nominativo', max_length=30),
        ),
        migrations.AlterField(
            model_name='client',
            name='surname',
            field=models.CharField(verbose_name='Cognome', max_length=30),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='name',
            field=models.CharField(verbose_name='Nome', max_length=30),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='surname',
            field=models.CharField(verbose_name='Cognome', max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_reservation',
            field=models.DateField(verbose_name='Data di prenotazione'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id_client',
            field=models.ForeignKey(verbose_name='Cliente', to='appOfficina.Client'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id_vehicle',
            field=models.ForeignKey(verbose_name='Veicolo', to='appOfficina.Vehicle'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='use',
            field=models.CharField(verbose_name='Uso', choices=[('c', 'Comunitario'), ('m', 'Medico'), ('p', 'Personali')], max_length=15),
        ),
    ]
