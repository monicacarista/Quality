# Generated by Django 3.2 on 2022-01-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0041_auto_20220120_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailpengecekan',
            name='raguragu',
            field=models.ManyToManyField(related_name='ragu', to='qc.MasterReject'),
        ),
        migrations.AlterField(
            model_name='detailpengecekan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='masterpilihan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='masterreject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='parameterdipilih',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pengecekan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]