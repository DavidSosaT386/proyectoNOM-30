# Generated by Django 3.1.7 on 2021-09-30 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='encuesta',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=1000)),
                ('categoria', models.CharField(choices=[('categoria1', 'Almacen'), ('categoria2', 'Oficina'), ('categoria3', 'Subestacion')], default='categoria1', max_length=50)),
            ],
            options={
                'verbose_name': 'encuesta',
                'verbose_name_plural': 'encuestas',
                'db_table': 'encuesta',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicion', models.BooleanField(default=False)),
                ('observacion', models.TextField(null=True)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminlte3.encuesta')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'respuesta',
                'verbose_name_plural': 'respuestas',
                'db_table': 'respuesta',
            },
        ),
    ]
