# Generated by Django 3.1.7 on 2021-11-14 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0006_auto_20211113_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='no_reporte',
            field=models.IntegerField(null=True),
        ),
    ]