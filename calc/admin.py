from django.contrib import admin
from .models import Scenario, Disease, Supply, TreatmentLine

# Register your models here.
admin.site.register(Scenario)
admin.site.register(Disease)

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display=['msf_code','supply_name','essential_item']
    

@admin.register(TreatmentLine)
class TreatmentLineAdmin(admin.ModelAdmin):
    list_display=['t_name', 'tline_disease', 'get_supplies']
    

