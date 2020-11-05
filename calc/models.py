from django.db import models
from django.conf import settings
import uuid

class Scenario(models.Model):
    #define attributes here
    scenario_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scenario_name=models.CharField(max_length=255, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    disease_6m_5yr=models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True) 
    disease_6m_15yr=models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    #also include order lead time?

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
    disease_attack_rate=models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    disease_hospitalisation_cases=models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    hospitalisation_length_stay=models.IntegerField(blank=True, null=True)
    peak_attack_rate=models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    incidence=models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    prevalence=models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    def __str__(self):
        return str(self.disease_name)

class Pharmacy(models.Model):
    #define attributes here
    medicine_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medicine_code=models.CharField(max_length=50)
    medicine_name=models.CharField(max_length=10000, null=True)
    disease_medicine=models.ManyToManyField(Disease)
    dosage=models.FloatField() #replace to avoid confusion 
    frequency=models.IntegerField()
    attrition_rate=models.FloatField()
    patients=models.IntegerField()
    six_mth_consumption=models.IntegerField()
    three_mth_consumption=models.IntegerField()
    last_order=models.IntegerField()
    
   
    #also include historic data fields
    
    @property
    def forecasted_amount(self):
        return self.dosage* self.frequency*self.patients * (1-self.attrition_rate)

    def __str__(self):
        return str(self.medicine_name)
        
    # added method to allow consumptioon comparison - not sure how this should be incorporated into forecasted_amount
    # maybe we need to first compare consumption and then add a correction factor to the forecast as opposed to the other way around
        
    # def compareConsumption(self,six_mth_consumption, three_mth_consumption, last_order, forecasted_amount):
    #     flag=False
    #     if self.forecasted_amount/self.six_mth_consumption>1:
    #         #set flag to True - pop up a banner that says "check consumption tool":
    #         self.flag=True
    #     elif self.forecasted_amount/self.three_mth_consumption>1:
    #         #...do something else
    #         pass

    #     else:
    #         # do something more
    #         pass
    #     return self.flag
    flat=compareConsumption(three_mth_consumption,six_mth_consumption,last_order)
    #define forecasted amount based on flag

class Patient(models.Model):
    # 
    pass

