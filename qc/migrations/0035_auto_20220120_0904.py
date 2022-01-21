# Generated by Django 3.0.1 on 2022-01-20 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0034_dtl_pengecekan_id_master_reject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dtl_pengecekan',
            old_name='tbl_rongga_atas',
            new_name='dimensi1',
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi10',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi11',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi12',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi2',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi3',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi4',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi5',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi6',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi7',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi8',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AddField(
            model_name='dtl_pengecekan',
            name='dimensi9',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='dtl_pengecekan',
            name='id_master_reject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.MasterReject', verbose_name='Jenis Reject'),
        ),
        migrations.AlterField(
            model_name='masterpilihan',
            name='nama_field',
            field=models.CharField(default=None, max_length=100, verbose_name='Parameter Pengecekan'),
        ),
        migrations.AlterField(
            model_name='masterreject',
            name='aspekCritical',
            field=models.CharField(choices=[('Critical', 'Critical'), ('Non Critical', 'Non Critical')], default='pilih salah satu', max_length=50, verbose_name='Aspek Critical'),
        ),
        migrations.AlterField(
            model_name='masterreject',
            name='aspekFungsional',
            field=models.CharField(choices=[('Fungsional', 'Fungsional'), ('Estetika', 'Estetika')], default='pilih salah satu', max_length=50, verbose_name='Aspek Fungsional'),
        ),
        migrations.AlterField(
            model_name='masterreject',
            name='aspekParameter',
            field=models.CharField(choices=[('Dimensi', 'Dimensi'), ('Atribut', 'Atribut')], default='pilih salah satu', max_length=50, verbose_name='Aspek Parameter'),
        ),
        migrations.AlterField(
            model_name='masterreject',
            name='id_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.MasterdataMastergroup', verbose_name='Grup Produk'),
        ),
        migrations.AlterField(
            model_name='masterreject',
            name='jenis_reject',
            field=models.CharField(default=None, max_length=50, verbose_name='Jenis Produk'),
        ),
        migrations.AlterField(
            model_name='parameterdipilih',
            name='field_dipilih',
            field=models.CharField(default=None, max_length=100, verbose_name='Parameter yang Dipilih'),
        ),
        migrations.AlterField(
            model_name='parameterdipilih',
            name='id_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.MasterdataMastergroup', verbose_name='Grup Produk'),
        ),
        migrations.AlterField(
            model_name='parameterdipilih',
            name='id_master_reject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.MasterReject', verbose_name='Jenis Reject'),
        ),
        migrations.AlterField(
            model_name='parameterdipilih',
            name='ket',
            field=models.CharField(default=None, max_length=100, verbose_name='Keterangan'),
        ),
        migrations.AlterField(
            model_name='pengecekan',
            name='id_group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.MasterdataMastergroup', verbose_name='Grup Produk'),
        ),
        migrations.AlterField(
            model_name='pengecekan',
            name='id_kk',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.FormProduksiKk', verbose_name='No KK'),
        ),
        migrations.AlterField(
            model_name='pengecekan',
            name='id_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='qc.AuthGroup', verbose_name='Kode Barang'),
        ),
    ]