# Generated by Django 3.1.3 on 2020-12-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_auto_20201208_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply',
            name='unit',
            field=models.CharField(blank=True, choices=[('mg', 'mg'), ('tab', 'tab')], max_length=5),
        ),
    ]
