from django.db import models
from django.conf import settings
import uuid

class Scenario(models.Model):
    #define attributes here
    scenario_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scenario_name=models.CharField(max_length=255, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    disease_6m_5yr=models.FloatField(default=None, blank=True, null=True) 
    disease_6m_15yr=models.FloatField(default=None, blank=True, null=True)
    order_lead_time=models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.scenario_name)
    
    # This should move to Pharmacy as they relate to the treatment and not the scenario? 
    #vaccine_coverage_objective=models.IntegerField(blank=True, null=True) 
    #vaccine_wasteage_percentage=models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)  
    #vaccine_buffer=models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True) 

class Disease(models.Model):
    #define attributes here
    disease_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scenario=models.ForeignKey(Scenario, on_delete=models.PROTECT)
    disease_name=models.CharField(max_length=255, blank=True, null=True)
    disease_alternative_names=models.CharField(max_length=255, blank=True, null=True)
    disease_attack_rate=models.FloatField(blank=True, null=True)
    disease_hospitalisation_cases=models.FloatField(blank=True, null=True)
    hospitalisation_length_stay=models.IntegerField(blank=True, null=True)
    peak_attack_rate=models.FloatField(blank=True, null=True)
    incidence=models.FloatField(blank=True, null=True)
    prevalence=models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.disease_name)

class Supply(models.Model):
    #define attributes here
    supply_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    msf_code=models.CharField(max_length=50, verbose_name='MSF Code', null=True, blank=True)
    supply_name=models.CharField(max_length=10000, null=True, verbose_name='Description')
    disease_supply=models.ManyToManyField(Disease, verbose_name='Condition')
    supply_frequency=models.CharField(max_length=10, blank=True, null=True, choices=[("0", "None"),("1", "1 x day"), ("2","2 x day"), (3,"3 x day"), (4, "4 x day"), (5, "5 x day")])
    #attrition_rate=models.FloatField(default=0)
    daily_recommended_dose=models.CharField(max_length=10, null=True, blank=True)
    patients_percentage=models.FloatField(verbose_name='Percentage of Patients', null=True, blank=True)
    essential_item=models.BooleanField(verbose_name='Essential NCD Item', null=True, blank=True)
    category=models.CharField(max_length=10000, choices=[('1','Medication'), ('2','Medical Equipment'), ('3','Medical Consumables'), ('4', 'Lab Equipment'), ('5','Lab Consumables')], blank=True, null=True)
    comments=models.CharField(max_length=10000, blank=True)
    unit=models.CharField(max_length=7, blank=True, choices=[('mg', 'mg'), ('tab','tab'), ('ampules', 'ampules'), ('vial', 'vial'), ('ml', 'ml'), ('IU', 'IU')] )
    
    
    class Meta:
        verbose_name_plural='Supplies'

    def __str__(self):
        return str(self.supply_name)
  

class TreatmentLine(models.Model):
    tline_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tline_disease=models.ForeignKey(Disease, verbose_name='Condition', on_delete=models.PROTECT)
    tline_name=models.CharField(max_length=10000, null=True, verbose_name='Treatment Line Name')    
    tline_supply=models.ManyToManyField(Supply, verbose_name='Supply')

    def __str__(self):
        return str(self.tline_name)

    def get_supplies(self):
        return [supply.supply_name for supply in self.tline_supply.all()]
    get_supplies.short_description='Supplies'
    
    def t_name(self):
        return str(self.tline_disease) +'-' +self.tline_name
    t_name.short_description='Treatment Line Name'
   