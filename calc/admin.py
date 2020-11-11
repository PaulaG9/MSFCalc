from django.contrib import admin
from .models import Scenario, Disease, Pharmacy

# Register your models here.
admin.site.register(Scenario)
admin.site.register(Disease)

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    readonly_fields=['forecasted_amount','flag2']
    list_display=['medicine_code','medicine_name','frequency', 'patients', 'forecasted_amount', 'flagger']
