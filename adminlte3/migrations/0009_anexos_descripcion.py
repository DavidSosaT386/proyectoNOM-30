# Generated by Django 3.1.7 on 2021-11-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0008_anexos'),
    ]

    operations = [
        migrations.AddField(
            model_name='anexos',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
