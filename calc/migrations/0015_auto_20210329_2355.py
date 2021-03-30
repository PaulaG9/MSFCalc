# Generated by Django 3.1.3 on 2021-03-29 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0014_auto_20210329_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentline',
            name='tline_description',
            field=models.CharField(max_length=10000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='supply',
            name='packaging_presentation',
            field=models.CharField(blank=True, choices=[('1', 'tablet'), ('2', 'ampule'), ('3', 'vial'), ('4', 'bottle')], max_length=10, null=True),
        ),
    ]