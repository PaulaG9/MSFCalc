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

class Pharmacy(models.Model):
    #define attributes here
    medicine_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    msf_code=models.CharField(max_length=50, verbose_name='MSF Code', null=True, blank=True)
    medicine_name=models.CharField(max_length=10000, null=True, verbose_name='Description')
    disease_medicine=models.ManyToManyField(Disease, verbose_name='Condition')
    frequency=models.FloatField(default=1)
    attrition_rate=models.FloatField(default=0)
    min_dosage=models.FloatField(null=True, blank=True)
    max_dosage=models.FloatField(null=True, blank=True)
    num_patients=models.FloatField(verbose_name='Number of Patients', default=1)
    essential_item=models.BooleanField(verbose_name='Essential NCD Item', null=True, blank=True)
    category=models.CharField(max_length=10000, choices=[('1','Medication'), ('2','Medical Equipment'), ('3','Medical Consumables'), ('4', 'Lab Equipment'), ('5','Lab Consumables')], blank=True, null=True)
    comments=models.CharField(max_length=10000, blank=True)
    
    
    class Meta:
        verbose_name_plural='Pharmacies'

    @property
    def forecasted_amount(self):
        if self.frequency==0  or self.num_patients==0 or self.attrition_rate==0:
            return 0
        else:
            try:
                return self.frequency*self.num_patients * (1-self.attrition_rate)
            except ValueError as e:
                print (e)
            

    def __str__(self):
        return str(self.medicine_name)
  

