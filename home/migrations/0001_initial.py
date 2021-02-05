# Generated by Django 3.1.3 on 2020-12-13 22:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, max_length=255, null=True)),
                ('disease_severity', models.CharField(choices=[('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')], max_length=7, verbose_name='Prevalence')),
            ],
        ),
    ]