# Generated by Django 3.0.1 on 2022-01-20 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0039_auto_20220120_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterpilihan',
            name='id_dtl_pengecekan',
        ),
    ]