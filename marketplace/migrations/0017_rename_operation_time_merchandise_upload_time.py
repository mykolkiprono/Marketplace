# Generated by Django 4.0.4 on 2022-10-13 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0016_remove_bussiness_dealing_type_bussiness_dealing_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchandise',
            old_name='operation_time',
            new_name='upload_time',
        ),
    ]
