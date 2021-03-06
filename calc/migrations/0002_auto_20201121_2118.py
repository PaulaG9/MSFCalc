# Generated by Django 3.1.3 on 2020-11-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pharmacy',
            options={'verbose_name_plural': 'Pharmacies'},
        ),
        migrations.RemoveField(
            model_name='pharmacy',
            name='dosage',
        ),
        migrations.RemoveField(
            model_name='pharmacy',
            name='medicine_code',
        ),
        migrations.AddField(
            model_name='disease',
            name='incidence',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disease',
            name='prevalence',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='attrition_rate',
            field=models.FloatField(default=0.2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='category',
            field=models.CharField(blank=True, choices=[(1, 'Medication'), (2, 'Medical Equipment'), (3, 'Medical Consumables'), (4, 'Lab Equipment'), (5, 'Lab Consumables')], max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='comments',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='essential_item',
            field=models.BooleanField(blank=True, null=True, verbose_name='Essential NCD Item'),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='max_dosage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='medicine_name',
            field=models.CharField(max_length=10000, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='min_dosage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='msf_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='MSF Code'),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='num_patients',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Patients'),
        ),
        migrations.AddField(
            model_name='scenario',
            name='order_lead_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='disease_attack_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='disease_hospitalisation_cases',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='peak_attack_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='disease_medicine',
            field=models.ManyToManyField(to='calc.Disease', verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='disease_6m_15yr',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='disease_6m_5yr',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
