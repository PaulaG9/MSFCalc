# Generated by Django 2.1.7 on 2020-11-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_auto_20201028_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='last_order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='six_mth_consumption',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='three_mth_consumption',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
