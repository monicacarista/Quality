# Generated by Django 3.1 on 2022-01-17 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0016_delete_tes'),
    ]

    operations = [
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='id_kk',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.formproduksikk'),
        ),
    ]
