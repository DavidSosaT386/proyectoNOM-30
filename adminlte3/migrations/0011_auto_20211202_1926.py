# Generated by Django 3.1.7 on 2021-12-03 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0010_auto_20211128_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='porfile',
            name='apellidos',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='porfile',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
