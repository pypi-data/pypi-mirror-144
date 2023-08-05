# Generated by Django 2.2.14 on 2020-08-28 21:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0081_remove_cameramodel_shutter_speeds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shutterspeed',
            name='shutter_speed',
            field=models.CharField(help_text='Shutter speed in fractional notation, e.g. 1/250', max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Shutter speed must be expressed like 1/125, 2, or 2.5', regex='^\\d+(/\\d+(\\.\\d+)?)?$')]),
        ),
    ]
