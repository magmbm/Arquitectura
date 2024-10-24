# Generated by Django 5.1.1 on 2024-10-24 00:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortalysis', '0002_errormortal_rename_causa_muerte_causaingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defuncion',
            name='FK_id_causa_ingreso',
            field=models.ForeignKey(db_column='causa_ingreso', default=1, on_delete=django.db.models.deletion.CASCADE, to='mortalysis.causaingreso'),
        ),
    ]
