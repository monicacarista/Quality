from dataclasses import fields
from django.contrib import admin
from qc.models import *
# Register your models here.

admin.site.site_header = 'DASHBOARD'


class PengecekanAdmin(admin.ModelAdmin):
    list_display = ['id_kk','id_name','kode_barang','id_group','tgl_pengecekan','shift_pengecekan','customer','mesin','get_namaOperator']
    search_fields = ['id_group']
    # list_filter = ['shift_pengecekan']
    list_per_page = 4
    # class Media:
    #     js=("admindrop/newajax.js")
    def get_namaOperator(self,obj):
        # print(obj.operator.nama_operator)
        return obj.operator.nama_operator
       
    get_namaOperator.admin_order_field = 'nama_operator'
    get_namaOperator.short_description = 'Nama Operator'

class DtlAdmin(admin.ModelAdmin):
    fields = [ 'dimensi1','raguragu']
    # list_display = ['']
    # search_fields = ['shift_pengecekan']
    # list_filter = ['shift_pengecekan']
    list_per_page = 5

    # def get_jenisReject(self,obj):
    #     return obj.operator.jenis_reject
    # get_jenisReject.admin_order_field = 'jenis_reject'
    # get_jenisReject.short_description = 'Jenis Reject'


class OperatorAdmin(admin.ModelAdmin):
    list_display = ['nama_operator']
    search_fields = ['nama_operator']
    list_per_page = 4

class MasterRejectAdmin(admin.ModelAdmin):
    list_display = ['jenis_reject']
    search_fields = ['jenis_reject']
    list_per_page = 4


# class ChoiceInLine(admin.StackedInline):
#     model = MasterPilihan
#     extra= 0 

class MasterPilihanAdmin(admin.ModelAdmin):
    
    fields = ['nama_field']
    list_display = ['nama_field']
    search_fields = ['nama_field']
    list_per_page = 10
    # inlines = [ChoiceInLine]



class MasterDipilihAdmin(admin.ModelAdmin):
    list_display = ['id_field_dipilih','ket','id_master_reject']
    search_fields = ['id_field_dipilih']
    list_per_page = 10

class TagInLineAdmin(admin.StackedInline):
    model = ParameterDipilih
    fields = [('id_field_dipilih','ket','id_master_reject')]
    extra= 0

class MasterDataMasterGroupAdmin(admin.ModelAdmin):
    model = MasterdataMastergroup
    inlines = [
        TagInLineAdmin,
    ]
    list_display = ['group','tipe']
    # fieldsets = [
    #     ( 'Group', {'fields' : ['group']}),
    #     # ('aaa', {'fields' : ['tipe']})
    # ]
    


admin.site.register(Pengecekan, PengecekanAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(DetailPengecekan,DtlAdmin)
admin.site.register(MasterReject,MasterRejectAdmin)
admin.site.register(MasterPilihan,MasterPilihanAdmin)
admin.site.register(ParameterDipilih,MasterDipilihAdmin)
admin.site.register(MasterdataMastergroup, MasterDataMasterGroupAdmin)
