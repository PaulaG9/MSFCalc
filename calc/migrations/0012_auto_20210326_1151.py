# Generated by Django 3.1.3 on 2021-03-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0011_auto_20210222_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='packaging_presentation',
            field=models.CharField(blank=True, choices=[('1', 'tablet'), ('2', 'ampules'), ('3', 'vial'), ('4', 'bottle')], max_length=10),
        ),
        migrations.AddField(
            model_name='supply',
            name='packaging_size',
            field=models.IntegerField(blank=True, null=True, verbose_name='Packaging Presentation'),
        ),
        migrations.AddField(
            model_name='supply',
            name='supply_strength',
            field=models.FloatField(blank=True, null=True, verbose_name='Supply Strength'),
        ),
        migrations.AlterField(
            model_name='supply',
            name='supply_frequency',
            field=models.CharField(blank=True, choices=[('0', 'None'), ('1', '1 x day'), ('2', '2 x day'), ('3', '3 x day'), ('4', '4 x day'), ('5', '5 x day')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='supply',
            name='unit',
            field=models.CharField(blank=True, choices=[('1', 'mg'), ('2', 'ml')], max_length=7),
        ),
    ]
