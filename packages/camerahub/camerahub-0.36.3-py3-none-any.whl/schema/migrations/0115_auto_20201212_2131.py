# Generated by Django 2.2.17 on 2020-12-12 21:31

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0114_auto_20201211_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlargermodel',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Image of the enlarger model', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='enlargermodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='enlargermodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AddField(
            model_name='flashmodel',
            name='disambiguation',
            field=models.CharField(blank=True, default='', help_text='Distinguishing notes for flash models with the same name', max_length=45),
        ),
        migrations.AddField(
            model_name='flashmodel',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Image of the flash model', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='flashmodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='flashmodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AddField(
            model_name='historicalenlargermodel',
            name='image',
            field=models.TextField(blank=True, help_text='Image of the enlarger model', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalenlargermodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='historicalenlargermodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AddField(
            model_name='historicalflashmodel',
            name='disambiguation',
            field=models.CharField(blank=True, default='', help_text='Distinguishing notes for flash models with the same name', max_length=45),
        ),
        migrations.AddField(
            model_name='historicalflashmodel',
            name='image',
            field=models.TextField(blank=True, help_text='Image of the flash model', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalflashmodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='historicalflashmodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AddField(
            model_name='historicalteleconvertermodel',
            name='disambiguation',
            field=models.CharField(blank=True, default='', help_text='Distinguishing notes for teleconverter models with the same name', max_length=45),
        ),
        migrations.AddField(
            model_name='historicalteleconvertermodel',
            name='image',
            field=models.TextField(blank=True, help_text='Image of the teleconverter model', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalteleconvertermodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='historicalteleconvertermodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AddField(
            model_name='teleconvertermodel',
            name='disambiguation',
            field=models.CharField(blank=True, default='', help_text='Distinguishing notes for teleconverter models with the same name', max_length=45),
        ),
        migrations.AddField(
            model_name='teleconvertermodel',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Image of the teleconverter model', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='teleconvertermodel',
            name='image_attribution',
            field=models.CharField(blank=True, help_text='Author of this image', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teleconvertermodel',
            name='image_attribution_url',
            field=models.URLField(blank=True, help_text='Attribution URL for this image', null=True),
        ),
        migrations.AlterField(
            model_name='enlargermodel',
            name='manufacturer',
            field=models.ForeignKey(help_text='Manufacturer of this enlarger', on_delete=django.db.models.deletion.CASCADE, to='schema.Manufacturer'),
        ),
        migrations.AlterField(
            model_name='flashmodel',
            name='manufacturer',
            field=models.ForeignKey(help_text='Manufacturer of this flash', on_delete=django.db.models.deletion.CASCADE, to='schema.Manufacturer'),
        ),
        migrations.AlterField(
            model_name='teleconvertermodel',
            name='manufacturer',
            field=models.ForeignKey(help_text='Manufacturer of this teleconverter', on_delete=django.db.models.deletion.CASCADE, to='schema.Manufacturer'),
        ),
        migrations.AddConstraint(
            model_name='flashmodel',
            constraint=models.UniqueConstraint(fields=('manufacturer', 'model', 'disambiguation'), name='flashmodel_unique_name'),
        ),
        migrations.AddConstraint(
            model_name='teleconvertermodel',
            constraint=models.UniqueConstraint(fields=('manufacturer', 'model', 'disambiguation'), name='teleconvertermodel_unique_name'),
        ),
    ]
