# Generated by Django 5.0.4 on 2024-05-01 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
        ('image_url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='image_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='image_url.imageurl'),
        ),
    ]
