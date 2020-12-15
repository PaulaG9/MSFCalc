from django.db import models
from django.conf import settings
import uuid

# Create your models here.
class Country(models.Model):
    country_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country_name=models.CharField(max_length=255, blank=True, null=True)
    disease_severity=models.CharField(max_length=7, choices=[('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')], verbose_name='Prevalence')
    country_iso=models.CharField(max_length=3, verbose_name='ISO Code')

    class Meta:
        verbose_name_plural='Countries'

    def __str__(self):
        return str(self.country_name)

    

