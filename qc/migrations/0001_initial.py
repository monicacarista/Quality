# Generated by Django 3.1 on 2022-01-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormMaintenanceBreakdownevent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=1)),
                ('no_form', models.CharField(max_length=32)),
                ('report_time', models.DateTimeField()),
                ('breakdown_note', models.TextField()),
            ],
            options={
                'db_table': 'form_maintenance_breakdownevent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormMaintenanceBreakdownfix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('breakdown_type', models.CharField(max_length=1)),
                ('fixing_note', models.TextField()),
            ],
            options={
                'db_table': 'form_maintenance_breakdownfix',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormMaintenanceBreakdownfixBrokenPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'form_maintenance_breakdownfix_broken_part',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormMaintenanceMastermachinepart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'form_maintenance_mastermachinepart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormMaintenanceMastermachinesection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'form_maintenance_mastermachinesection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormMaintenanceMastertechnician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'form_maintenance_mastertechnician',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormProduksiDetaildowntime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_mulai', models.TimeField()),
                ('waktu_selesai', models.TimeField()),
                ('kategori', models.CharField(max_length=2)),
                ('notes', models.TextField()),
                ('durasi', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'form_produksi_detaildowntime',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormProduksiDetailkkfinishedgood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_qty', models.FloatField()),
            ],
            options={
                'db_table': 'form_produksi_detailkkfinishedgood',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormProduksiDetailkkrawmaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
            ],
            options={
                'db_table': 'form_produksi_detailkkrawmaterial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormProduksiDetailmaterialconsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_awal', models.FloatField()),
                ('qty_tambahan', models.FloatField()),
                ('qty_akhir', models.FloatField()),
                ('batch_no', models.CharField(blank=True, max_length=20, null=True)),
                ('qty_pakai', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'form_produksi_detailmaterialconsumption',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormProduksiDetailpackagingusage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terpakai', models.FloatField()),
                ('reject', models.FloatField()),
            ],
            options={
                'db_table': 'form_produksi_detailpackagingusage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormProduksiDetailproductionresults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasil_jadi_qty', models.FloatField()),
                ('hold_qc_qty', models.FloatField()),
                ('berat_unit_sample', models.FloatField()),
                ('reject', models.FloatField()),
                ('trimming', models.FloatField()),
                ('waste', models.FloatField()),
                ('batch_no', models.CharField(blank=True, max_length=20, null=True)),
                ('fg_mass', models.FloatField(blank=True, null=True)),
                ('hold_mass', models.FloatField(blank=True, null=True)),
                ('total_output', models.FloatField(blank=True, null=True)),
                ('fg_lm', models.FloatField(blank=True, null=True)),
                ('fg_m2', models.FloatField(blank=True, null=True)),
                ('fg_mass_std', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'form_produksi_detailproductionresults',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormProduksiKk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_kk', models.CharField(max_length=20, unique=True)),
                ('aktif', models.CharField(max_length=1)),
                ('is_export', models.CharField(max_length=1)),
                ('cleaning', models.IntegerField()),
                ('trial', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('creation_date', models.DateField()),
            ],
            options={
                'db_table': 'form_produksi_kk',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormProduksiProductionform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreman_id', models.IntegerField(blank=True, null=True)),
                ('shift', models.CharField(max_length=1)),
                ('user_group_id', models.IntegerField()),
                ('dl_avail', models.FloatField()),
                ('reject', models.FloatField(blank=True, null=True)),
                ('downtime', models.FloatField(blank=True, null=True)),
                ('earn_hour', models.FloatField(blank=True, null=True)),
                ('effective_hour', models.FloatField(blank=True, null=True)),
                ('fg', models.FloatField(blank=True, null=True)),
                ('hold', models.FloatField(blank=True, null=True)),
                ('raw_material', models.FloatField(blank=True, null=True)),
                ('scrap_usage', models.FloatField(blank=True, null=True)),
                ('total_hour', models.FloatField(blank=True, null=True)),
                ('trimming', models.FloatField(blank=True, null=True)),
                ('waste', models.FloatField(blank=True, null=True)),
                ('fg_qty', models.FloatField(blank=True, null=True)),
                ('reject_eqv', models.FloatField(blank=True, null=True)),
                ('end_time', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('planned_down_hour', models.FloatField(blank=True, null=True)),
                ('scrap_hasil', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('output_std', models.FloatField(blank=True, null=True)),
                ('catatan', models.TextField(blank=True, null=True)),
                ('total_output', models.FloatField(blank=True, null=True)),
                ('fg_lm', models.FloatField(blank=True, null=True)),
                ('fg_m2', models.FloatField(blank=True, null=True)),
                ('byproduct', models.FloatField(blank=True, null=True)),
                ('fg_mass_std', models.FloatField(blank=True, null=True)),
                ('normalized_date', models.DateTimeField(blank=True, null=True)),
                ('rm_split', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'form_produksi_productionform',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataDayofflist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off_day', models.DateField()),
                ('notes', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'masterdata_dayofflist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataGroupprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_type', models.CharField(max_length=1)),
                ('shift_hour', models.BigIntegerField()),
                ('daily_work_hour', models.FloatField()),
                ('weekly_days', models.CharField(max_length=7)),
                ('admin_email', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'masterdata_groupprofile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMasterbarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=70)),
                ('kode_barang', models.CharField(max_length=50, unique=True)),
                ('panjang', models.IntegerField()),
                ('tebal1', models.FloatField()),
                ('tebal2', models.FloatField(blank=True, null=True)),
                ('lebar', models.FloatField()),
                ('aktif', models.CharField(max_length=1)),
                ('gsm', models.FloatField(blank=True, null=True)),
                ('lebar_ext', models.FloatField(blank=True, null=True)),
                ('bobot_reject', models.FloatField(blank=True, null=True)),
                ('berat_standar_fg', models.FloatField()),
            ],
            options={
                'db_table': 'masterdata_masterbarang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMastergroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=40)),
                ('kategori_rm', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'masterdata_mastergroup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMasteritemproperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'masterdata_masteritemproperty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMasterkapasitasmesin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_ideal', models.FloatField()),
                ('dl_standar', models.FloatField()),
                ('tebal', models.FloatField(blank=True, null=True)),
                ('dimensi_aux', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'masterdata_masterkapasitasmesin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMastermesin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesin', models.CharField(max_length=30)),
                ('add_date', models.DateField()),
                ('priority', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'masterdata_mastermesin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMasterstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'masterdata_masterstatus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMastertipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'masterdata_mastertipe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMasteruom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'masterdata_masteruom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMasterwarna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warna', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'masterdata_masterwarna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataMasterworker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('aktif', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'masterdata_masterworker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataUserprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'masterdata_userprofile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterdataUserprofileFactoryGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'masterdata_userprofile_factory_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbase', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('query', models.TextField()),
            ],
            options={
                'db_table': 'pma__bookmark',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaCentralColumns',
            fields=[
                ('db_name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('col_name', models.CharField(max_length=64)),
                ('col_type', models.CharField(max_length=64)),
                ('col_length', models.TextField(blank=True, null=True)),
                ('col_collation', models.CharField(max_length=64)),
                ('col_isnull', models.IntegerField(db_column='col_isNull')),
                ('col_extra', models.CharField(blank=True, max_length=255, null=True)),
                ('col_default', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pma__central_columns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaColumnInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=64)),
                ('table_name', models.CharField(max_length=64)),
                ('column_name', models.CharField(max_length=64)),
                ('comment', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=255)),
                ('transformation', models.CharField(max_length=255)),
                ('transformation_options', models.CharField(max_length=255)),
                ('input_transformation', models.CharField(max_length=255)),
                ('input_transformation_options', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'pma__column_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaDesignerSettings',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('settings_data', models.TextField()),
            ],
            options={
                'db_table': 'pma__designer_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaExportTemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('export_type', models.CharField(max_length=10)),
                ('template_name', models.CharField(max_length=64)),
                ('template_data', models.TextField()),
            ],
            options={
                'db_table': 'pma__export_templates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaFavorite',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('tables', models.TextField()),
            ],
            options={
                'db_table': 'pma__favorite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64)),
                ('db', models.CharField(max_length=64)),
                ('table', models.CharField(max_length=64)),
                ('timevalue', models.DateTimeField()),
                ('sqlquery', models.TextField()),
            ],
            options={
                'db_table': 'pma__history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaNavigationhiding',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=64)),
                ('item_type', models.CharField(max_length=64)),
                ('db_name', models.CharField(max_length=64)),
                ('table_name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'pma__navigationhiding',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaPdfPages',
            fields=[
                ('db_name', models.CharField(max_length=64)),
                ('page_nr', models.AutoField(primary_key=True, serialize=False)),
                ('page_descr', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'pma__pdf_pages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaRecent',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('tables', models.TextField()),
            ],
            options={
                'db_table': 'pma__recent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaRelation',
            fields=[
                ('master_db', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('master_table', models.CharField(max_length=64)),
                ('master_field', models.CharField(max_length=64)),
                ('foreign_db', models.CharField(max_length=64)),
                ('foreign_table', models.CharField(max_length=64)),
                ('foreign_field', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'pma__relation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaSavedsearches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('db_name', models.CharField(max_length=64)),
                ('search_name', models.CharField(max_length=64)),
                ('search_data', models.TextField()),
            ],
            options={
                'db_table': 'pma__savedsearches',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaTableCoords',
            fields=[
                ('db_name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('table_name', models.CharField(max_length=64)),
                ('pdf_page_number', models.IntegerField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
            ],
            options={
                'db_table': 'pma__table_coords',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaTableInfo',
            fields=[
                ('db_name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('table_name', models.CharField(max_length=64)),
                ('display_field', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'pma__table_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaTableUiprefs',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('db_name', models.CharField(max_length=64)),
                ('table_name', models.CharField(max_length=64)),
                ('prefs', models.TextField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'pma__table_uiprefs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaTracking',
            fields=[
                ('db_name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('table_name', models.CharField(max_length=64)),
                ('version', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('schema_snapshot', models.TextField()),
                ('schema_sql', models.TextField(blank=True, null=True)),
                ('data_sql', models.TextField(blank=True, null=True)),
                ('tracking', models.CharField(blank=True, max_length=188, null=True)),
                ('tracking_active', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'pma__tracking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaUserconfig',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('timevalue', models.DateTimeField()),
                ('config_data', models.TextField()),
            ],
            options={
                'db_table': 'pma__userconfig',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaUsergroups',
            fields=[
                ('usergroup', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('tab', models.CharField(max_length=64)),
                ('allowed', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'pma__usergroups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PmaUsers',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('usergroup', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'pma__users',
                'managed': False,
            },
        ),
    ]