# Generated by Django 3.1.7 on 2021-12-06 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0011_auto_20211202_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porfile',
            name='centro_trabajo',
            field=models.CharField(choices=[('sede', 'sede'), ('Villahermosa', 'Villahermosa'), ('Tuxtla gutierrez', 'Tuxtla gutierrez'), ('Tapachula', 'Tapachula'), ('Itsmo', 'Itsmo'), ('Malpaso', 'Malpaso'), ('Zotze', 'Zotze')], default='sede', max_length=80),
        ),
    ]
