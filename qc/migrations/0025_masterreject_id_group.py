# Generated by Django 3.1 on 2022-01-18 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0024_auto_20220118_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterreject',
            name='id_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.masterdatamastergroup'),
        ),
    ]
