# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from dataclasses import field
from statistics import mode
from tabnanny import verbose
from tkinter import Widget
from django.db import models
from django.utils.timezone import now
from multiselectfield import MultiSelectField
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import ModelForm
 

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
    def __str__(self):
         return self.name   


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FormMaintenanceBreakdownevent(models.Model):
    status = models.CharField(max_length=1)
    no_form = models.CharField(max_length=32)
    report_time = models.DateTimeField()
    breakdown_note = models.TextField()
    machine = models.ForeignKey('MasterdataMastermesin', models.DO_NOTHING)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'form_maintenance_breakdownevent'


class FormMaintenanceBreakdownfix(models.Model):
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    breakdown_type = models.CharField(max_length=1)
    fixing_note = models.TextField()
    breakdown_event = models.OneToOneField(FormMaintenanceBreakdownevent, models.DO_NOTHING)
    broken_section = models.ForeignKey('FormMaintenanceMastermachinesection', models.DO_NOTHING)
    technician = models.ForeignKey('FormMaintenanceMastertechnician', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'form_maintenance_breakdownfix'


class FormMaintenanceBreakdownfixBrokenPart(models.Model):
    breakdownfix = models.ForeignKey(FormMaintenanceBreakdownfix, models.DO_NOTHING)
    mastermachinepart = models.ForeignKey('FormMaintenanceMastermachinepart', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'form_maintenance_breakdownfix_broken_part'
        unique_together = (('breakdownfix', 'mastermachinepart'),)


class FormMaintenanceMastermachinepart(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'form_maintenance_mastermachinepart'


class FormMaintenanceMastermachinesection(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'form_maintenance_mastermachinesection'


class FormMaintenanceMastertechnician(models.Model):
    name = models.CharField(max_length=32)
    status = models.CharField(max_length=1)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'form_maintenance_mastertechnician'


class FormProduksiDetaildowntime(models.Model):
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    kategori = models.CharField(max_length=2)
    notes = models.TextField()
    laporan = models.ForeignKey('FormProduksiProductionform', models.DO_NOTHING)
    durasi = models.FloatField(blank=True, null=True)
    form_breakdown = models.ForeignKey(FormMaintenanceBreakdownevent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_produksi_detaildowntime'


class FormProduksiDetailkkfinishedgood(models.Model):
    order_qty = models.FloatField()
    no_kk = models.ForeignKey('FormProduksiKk', models.DO_NOTHING)
    produk = models.ForeignKey('MasterdataMasterbarang', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'form_produksi_detailkkfinishedgood'


class FormProduksiDetailkkrawmaterial(models.Model):
    qty = models.FloatField()
    bahan = models.ForeignKey('MasterdataMasterbarang', models.DO_NOTHING)
    no_kk = models.ForeignKey('FormProduksiKk', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'form_produksi_detailkkrawmaterial'


class FormProduksiDetailmaterialconsumption(models.Model):
    qty_awal = models.FloatField()
    qty_tambahan = models.FloatField()
    qty_akhir = models.FloatField()
    bahan = models.ForeignKey('MasterdataMasterbarang', models.DO_NOTHING)
    laporan = models.ForeignKey('FormProduksiProductionform', models.DO_NOTHING)
    batch_no = models.CharField(max_length=20, blank=True, null=True)
    qty_pakai = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_produksi_detailmaterialconsumption'


class FormProduksiDetailpackagingusage(models.Model):
    terpakai = models.FloatField()
    reject = models.FloatField()
    laporan = models.ForeignKey('FormProduksiProductionform', models.DO_NOTHING)
    packaging = models.ForeignKey('MasterdataMasterbarang', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'form_produksi_detailpackagingusage'


class FormProduksiDetailproductionresults(models.Model):
    hasil_jadi_qty = models.FloatField()
    hold_qc_qty = models.FloatField()
    berat_unit_sample = models.FloatField()
    reject = models.FloatField()
    trimming = models.FloatField()
    waste = models.FloatField()
    laporan = models.ForeignKey('FormProduksiProductionform', models.DO_NOTHING)
    produk = models.ForeignKey('MasterdataMasterbarang', models.DO_NOTHING)
    batch_no = models.CharField(max_length=20, blank=True, null=True)
    fg_mass = models.FloatField(blank=True, null=True)
    hold_mass = models.FloatField(blank=True, null=True)
    total_output = models.FloatField(blank=True, null=True)
    fg_lm = models.FloatField(blank=True, null=True)
    fg_m2 = models.FloatField(blank=True, null=True)
    fg_mass_std = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_produksi_detailproductionresults'


class FormProduksiKk(models.Model):
    no_kk = models.CharField(unique=True, max_length=20)
    aktif = models.CharField(max_length=1)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    is_export = models.CharField(max_length=1)
    cleaning = models.IntegerField()
    trial = models.IntegerField()
    created_at = models.DateTimeField()
    creation_date = models.DateField()
    item_example = models.ForeignKey('MasterdataMasterbarang', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_produksi_kk'

    def __str__(self):
        return self.no_kk

class FormProduksiProductionform(models.Model):
    foreman_id = models.IntegerField(blank=True, null=True)
    machine = models.ForeignKey('MasterdataMastermesin', models.DO_NOTHING)
    no_kk = models.ForeignKey(FormProduksiKk, models.DO_NOTHING)
    shift = models.CharField(max_length=1)
    user_group_id = models.IntegerField()
    dl_avail = models.FloatField()
    reject = models.FloatField(blank=True, null=True)
    downtime = models.FloatField(blank=True, null=True)
    earn_hour = models.FloatField(blank=True, null=True)
    effective_hour = models.FloatField(blank=True, null=True)
    fg = models.FloatField(blank=True, null=True)
    hold = models.FloatField(blank=True, null=True)
    raw_material = models.FloatField(blank=True, null=True)
    scrap_usage = models.FloatField(blank=True, null=True)
    total_hour = models.FloatField(blank=True, null=True)
    trimming = models.FloatField(blank=True, null=True)
    waste = models.FloatField(blank=True, null=True)
    group_barang = models.ForeignKey('MasterdataMastergroup', models.DO_NOTHING, blank=True, null=True)
    fg_qty = models.FloatField(blank=True, null=True)
    reject_eqv = models.FloatField(blank=True, null=True)
    end_time = models.DateTimeField()
    start_time = models.DateTimeField()
    planned_down_hour = models.FloatField(blank=True, null=True)
    scrap_hasil = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    output_std = models.FloatField(blank=True, null=True)
    catatan = models.TextField(blank=True, null=True)
    tipe_barang = models.ForeignKey('MasterdataMastertipe', models.DO_NOTHING, blank=True, null=True)
    total_output = models.FloatField(blank=True, null=True)
    fg_lm = models.FloatField(blank=True, null=True)
    fg_m2 = models.FloatField(blank=True, null=True)
    byproduct = models.FloatField(blank=True, null=True)
    operator = models.ForeignKey('MasterdataMasterworker', models.DO_NOTHING, blank=True, null=True)
    fg_mass_std = models.FloatField(blank=True, null=True)
    normalized_date = models.DateTimeField(blank=True, null=True)
    rm_split = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_produksi_productionform'


class MasterdataDayofflist(models.Model):
    off_day = models.DateField()
    notes = models.CharField(max_length=50)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'masterdata_dayofflist'


class MasterdataGroupprofile(models.Model):
    group_type = models.CharField(max_length=1)
    user_group = models.OneToOneField(AuthGroup, models.DO_NOTHING)
    shift_hour = models.BigIntegerField()
    daily_work_hour = models.FloatField()
    weekly_days = models.CharField(max_length=7)
    admin_email = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masterdata_groupprofile'


class MasterdataMasterbarang(models.Model):
    nama = models.CharField(max_length=70)
    kode_barang = models.CharField(unique=True, max_length=50)
    panjang = models.IntegerField()
    tebal1 = models.FloatField()
    tebal2 = models.FloatField(blank=True, null=True)
    group = models.ForeignKey('MasterdataMastergroup', models.DO_NOTHING)
    tipe = models.ForeignKey('MasterdataMastertipe', models.DO_NOTHING)
    uom = models.ForeignKey('MasterdataMasteruom', models.DO_NOTHING)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    warna = models.ForeignKey('MasterdataMasterwarna', models.DO_NOTHING, blank=True, null=True)
    lebar = models.FloatField()
    aktif = models.CharField(max_length=1)
    gsm = models.FloatField(blank=True, null=True)
    lebar_ext = models.FloatField(blank=True, null=True)
    bobot_reject = models.FloatField(blank=True, null=True)
    berat_standar_fg = models.FloatField()
    profil = models.ForeignKey('MasterdataMasteritemproperty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'masterdata_masterbarang'

    def __str__(self):
         return self.kode_barang

class MasterdataMastergroup(models.Model):
    group = models.CharField(max_length=40)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    tipe = models.ForeignKey('MasterdataMastertipe', models.DO_NOTHING)
    kategori_rm = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masterdata_mastergroup'
    
    def __str__(self):
         return self.group


class MasterdataMasteritemproperty(models.Model):
    prop = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'masterdata_masteritemproperty'


class MasterdataMasterkapasitasmesin(models.Model):
    output_ideal = models.FloatField()
    dl_standar = models.FloatField()
    group = models.ForeignKey(MasterdataMastergroup, models.DO_NOTHING, blank=True, null=True)
    mesin = models.ForeignKey('MasterdataMastermesin', models.DO_NOTHING)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    warna = models.ForeignKey('MasterdataMasterwarna', models.DO_NOTHING, blank=True, null=True)
    tebal = models.FloatField(blank=True, null=True)
    prop = models.ForeignKey(MasterdataMasteritemproperty, models.DO_NOTHING, blank=True, null=True)
    dimensi_aux = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masterdata_masterkapasitasmesin'


class MasterdataMastermesin(models.Model):
    mesin = models.CharField(max_length=30)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    add_date = models.DateField()
    priority = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'masterdata_mastermesin'

    def __str__(self):
         return self.mesin

class MasterdataMasterstatus(models.Model):
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'masterdata_masterstatus'


class MasterdataMastertipe(models.Model):
    tipe = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'masterdata_mastertipe'


class MasterdataMasteruom(models.Model):
    uom = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'masterdata_masteruom'


class MasterdataMasterwarna(models.Model):
    warna = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'masterdata_masterwarna'


class MasterdataMasterworker(models.Model):
    nama = models.CharField(max_length=50)
    aktif = models.CharField(max_length=1)
    status = models.ForeignKey(MasterdataMasterstatus, models.DO_NOTHING)
    user_group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'masterdata_masterworker'


class MasterdataUserprofile(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    main_group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masterdata_userprofile'


class MasterdataUserprofileFactoryGroup(models.Model):
    userprofile = models.ForeignKey(MasterdataUserprofile, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'masterdata_userprofile_factory_group'
        unique_together = (('userprofile', 'group'),)


class PmaBookmark(models.Model):
    dbase = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    query = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__bookmark'


class PmaCentralColumns(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    col_name = models.CharField(max_length=64)
    col_type = models.CharField(max_length=64)
    col_length = models.TextField(blank=True, null=True)
    col_collation = models.CharField(max_length=64)
    col_isnull = models.IntegerField(db_column='col_isNull')  # Field name made lowercase.
    col_extra = models.CharField(max_length=255, blank=True, null=True)
    col_default = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma__central_columns'
        unique_together = (('db_name', 'col_name'),)


class PmaColumnInfo(models.Model):
    db_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)
    column_name = models.CharField(max_length=64)
    comment = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=255)
    transformation = models.CharField(max_length=255)
    transformation_options = models.CharField(max_length=255)
    input_transformation = models.CharField(max_length=255)
    input_transformation_options = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pma__column_info'
        unique_together = (('db_name', 'table_name', 'column_name'),)


class PmaDesignerSettings(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    settings_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__designer_settings'


class PmaExportTemplates(models.Model):
    username = models.CharField(max_length=64)
    export_type = models.CharField(max_length=10)
    template_name = models.CharField(max_length=64)
    template_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__export_templates'
        unique_together = (('username', 'export_type', 'template_name'),)


class PmaFavorite(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    tables = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__favorite'


class PmaHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=64)
    db = models.CharField(max_length=64)
    table = models.CharField(max_length=64)
    timevalue = models.DateTimeField()
    sqlquery = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__history'


class PmaNavigationhiding(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    item_name = models.CharField(max_length=64)
    item_type = models.CharField(max_length=64)
    db_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pma__navigationhiding'
        unique_together = (('username', 'item_name', 'item_type', 'db_name', 'table_name'),)


class PmaPdfPages(models.Model):
    db_name = models.CharField(max_length=64)
    page_nr = models.AutoField(primary_key=True)
    page_descr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pma__pdf_pages'


class PmaRecent(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    tables = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__recent'


class PmaRelation(models.Model):
    master_db = models.CharField(primary_key=True, max_length=64)
    master_table = models.CharField(max_length=64)
    master_field = models.CharField(max_length=64)
    foreign_db = models.CharField(max_length=64)
    foreign_table = models.CharField(max_length=64)
    foreign_field = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pma__relation'
        unique_together = (('master_db', 'master_table', 'master_field'),)


class PmaSavedsearches(models.Model):
    username = models.CharField(max_length=64)
    db_name = models.CharField(max_length=64)
    search_name = models.CharField(max_length=64)
    search_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__savedsearches'
        unique_together = (('username', 'db_name', 'search_name'),)


class PmaTableCoords(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    pdf_page_number = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pma__table_coords'
        unique_together = (('db_name', 'table_name', 'pdf_page_number'),)


class PmaTableInfo(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    display_field = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pma__table_info'
        unique_together = (('db_name', 'table_name'),)


class PmaTableUiprefs(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    db_name = models.CharField(max_length=64)
    table_name = models.CharField(max_length=64)
    prefs = models.TextField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pma__table_uiprefs'
        unique_together = (('username', 'db_name', 'table_name'),)


class PmaTracking(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    version = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    schema_snapshot = models.TextField()
    schema_sql = models.TextField(blank=True, null=True)
    data_sql = models.TextField(blank=True, null=True)
    tracking = models.CharField(max_length=188, blank=True, null=True)
    tracking_active = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pma__tracking'
        unique_together = (('db_name', 'table_name', 'version'),)


class PmaUserconfig(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    timevalue = models.DateTimeField()
    config_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pma__userconfig'


class PmaUsergroups(models.Model):
    usergroup = models.CharField(primary_key=True, max_length=64)
    tab = models.CharField(max_length=64)
    allowed = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'pma__usergroups'
        unique_together = (('usergroup', 'tab', 'allowed'),)


class PmaUsers(models.Model):
    username = models.CharField(primary_key=True, max_length=64)
    usergroup = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'pma__users'
        unique_together = (('username', 'usergroup'),)


class Pengecekan(models.Model):
    shift_choices=(
    ('1','1'),
    ('2', '2'),
    ('3','3'),
    )
    id_group = models.ForeignKey('qc.MasterdataMastergroup', default=None, on_delete = models.CASCADE,  verbose_name="Grup Produk")
    id_kk = models.ForeignKey('qc.FormProduksiKk', default=None, on_delete = models.CASCADE,  verbose_name="No KK")
    id_name = models.ForeignKey('qc.AuthGroup',default=None, on_delete=models.CASCADE,  verbose_name="Unit")
    kode_barang =models.ForeignKey('qc.MasterdataMasterbarang',default=None, on_delete=models.CASCADE, verbose_name="Kode Barang")
    shift_pengecekan = models.CharField(max_length=1, default="pilih salah satu", choices=shift_choices)
    operator= models.ForeignKey('qc.Operator', default=None, on_delete=models.CASCADE)
    tgl_pengecekan = models.DateTimeField('Tanggal Pengecekan',default=now, blank=True)
    customer = models.CharField(max_length=30,default=None)
    mesin = models.ForeignKey('qc.MasterdataMastermesin',max_length=30, default=None, on_delete=models.CASCADE)

    def __str__(self):
         return '{} {}'.format(self.shift_pengecekan, self.tgl_pengecekan)

class Operator(models.Model):
    nama_operator = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = 'Operator'
    def __str__(self):
         return self.nama_operator


class MasterReject(models.Model):
    aspek_fungsional=  (
        ('Fungsional','Fungsional'), 
        ('Estetika', 'Estetika')
    )
    aspek_parameter =(
        ('Dimensi','Dimensi'),
        ('Atribut','Atribut')
    )
    aspek_critical=(
        ('Critical','Critical'),
        ('Non Critical','Non Critical')
    )
    id_group = models.ForeignKey('qc.MasterdataMastergroup', verbose_name="Grup Produk",default=None, on_delete=models.CASCADE)
    jenis_reject = models.CharField(max_length=50, default=None, verbose_name = "Jenis Reject")
    aspekFungsional = models.CharField(max_length=50, default="pilih salah satu", choices=aspek_fungsional, verbose_name= "Aspek Fungsional")
    aspekParameter = models.CharField(max_length=50, default="pilih salah satu", choices=aspek_parameter, verbose_name= "Aspek Parameter")
    aspekCritical = models.CharField(max_length=50, default="pilih salah satu", choices=aspek_critical, verbose_name= "Aspek Critical")
    ragu2 = models
    class Meta:
        verbose_name = 'Jenis Reject'
    def __str__(self):
         return self.jenis_reject

class MasterPilihan(models.Model):
    nama_field = models.CharField(max_length= 100,default=None,  verbose_name="Parameter Pengecekan")
    
    def __str__(self):
         return self.nama_field


class ParameterDipilih(models.Model):
      id_group = models.ForeignKey('qc.MasterdataMastergroup', default=None, on_delete=models.CASCADE,  verbose_name="Grup Produk")
      id_master_reject = models.ForeignKey('qc.MasterReject',  verbose_name="Jenis Reject", default=None, on_delete=models.CASCADE)
      id_field_dipilih = models.ForeignKey('qc.MasterPilihan',  verbose_name="Parameter yang Dipilih", default=None, on_delete=models.CASCADE)
      ket = models.CharField(max_length=100, default=None,  verbose_name= "Keterangan")

      def __str__(self):
         return self.id_field_dipilih.__str__()
         

class DetailPengecekan(models.Model):
    id_pengecekan=models.ForeignKey('qc.Pengecekan',null=True, default=None, on_delete=models.CASCADE)
    id_master_reject = models.ForeignKey('qc.MasterReject',null=True, default=None, on_delete=models.CASCADE,  verbose_name="Jenis Reject")
    dimensi1=models.CharField(max_length=5,default=None)
    dimensi2=models.CharField(max_length=5,default=None)
    dimensi3=models.CharField(max_length=5,default=None)
    dimensi4=models.CharField(max_length=5,default=None)
    dimensi5=models.CharField(max_length=5,default=None)
    dimensi6=models.CharField(max_length=5,default=None)
    dimensi7=models.CharField(max_length=5,default=None)
    dimensi8=models.CharField(max_length=5,default=None)
    dimensi9=models.CharField(max_length=5,default=None)
    dimensi10=models.CharField(max_length=5,default=None)
    dimensi11=models.CharField(max_length=5,default=None)
    dimensi12=models.CharField(max_length=5,default=None)
    raguragu = models.ManyToManyField('qc.MasterReject', related_name='ragu')
    
    class Meta:
        verbose_name = 'Detail Pengecekan'
        verbose_name_plural = 'Dtl_Pengecekan'

    def __str__(self):
         return self.dimensi1

class DetailForm(ModelForm):

    class Meta:
        model = DetailPengecekan
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super(DetailForm, self).__init__(*args, **kwargs)

        self.fields["raguragu"].widget =  CheckboxSelectMultiple()
        self.fields["raguragu"].queryset = MasterReject.objects.all()
