# Generated by Django 3.1 on 2022-01-12 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0008_dtl_pengecekan'),
    ]

    operations = [
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='tbl_rongga_atas',
            field=models.CharField(default=None, max_length=5),
        ),
    ]
