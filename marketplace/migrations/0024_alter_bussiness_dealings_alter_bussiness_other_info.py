# Generated by Django 4.0.4 on 2022-10-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0023_remove_bussiness_location_bussiness_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussiness',
            name='dealings',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='bussiness',
            name='other_info',
            field=models.CharField(max_length=200, null=True),
        ),
    ]