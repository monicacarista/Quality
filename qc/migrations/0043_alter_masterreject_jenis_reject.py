# Generated by Django 3.2 on 2022-01-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0042_auto_20220120_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterreject',
            name='jenis_reject',
            field=models.CharField(default=None, max_length=50, verbose_name='Jenis Reject'),
        ),
    ]
