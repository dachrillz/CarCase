# Generated by Django 2.1.3 on 2018-11-19 22:09

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_totalsales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalsales',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
