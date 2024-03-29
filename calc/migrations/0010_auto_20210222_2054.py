# Generated by Django 3.1.3 on 2021-02-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_auto_20201213_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supply',
            name='max_dosage',
        ),
        migrations.RemoveField(
            model_name='supply',
            name='min_dosage',
        ),
        migrations.AddField(
            model_name='supply',
            name='daily_dose',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='supply',
            name='patients_percentage',
            field=models.FloatField(blank=True, null=True, verbose_name='Percentage of Patients'),
        ),
        migrations.AddField(
            model_name='supply',
            name='supply_frequency',
            field=models.CharField(blank=True, choices=[(0, 'None'), (1, '1 x day'), (2, '2 x day'), (3, '3 x day'), (4, '4 x day'), (5, '5 x day')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='supply',
            name='unit',
            field=models.CharField(blank=True, choices=[('mg', 'mg'), ('tab', 'tab'), ('ampules', 'ampules'), ('vial', 'vial'), ('ml', 'ml'), ('IU', 'IU')], max_length=7),
        ),
    ]
