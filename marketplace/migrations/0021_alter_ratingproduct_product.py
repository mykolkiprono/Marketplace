# Generated by Django 4.0.4 on 2022-10-13 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0020_newsreads_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.merchandise'),
        ),
    ]