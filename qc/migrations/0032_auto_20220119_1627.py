# Generated by Django 3.0.1 on 2022-01-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0031_auto_20220119_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterreject',
            name='kategori',
        ),
        migrations.AddField(
            model_name='masterreject',
            name='aspekFungsional',
            field=models.CharField(choices=[('Fungsional', 'Fungsional'), ('Estetika', 'Estetika')], default='pilih salah satu', max_length=50),
        ),
        migrations.AddField(
            model_name='masterreject',
            name='aspekParameter',
            field=models.CharField(choices=[('Dimensi', 'Dimensi'), ('Atribut', 'Atribut')], default='pilih salah satu', max_length=50),
        ),
    ]
