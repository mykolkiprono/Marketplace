# Generated by Django 4.0.4 on 2022-10-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0011_alter_expertise_county'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expertise',
            name='dealing_type',
        ),
        migrations.AddField(
            model_name='expertise',
            name='dealing_list',
            field=models.CharField(default='selling', max_length=50),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/logos'),
        ),
    ]
