# Generated by Django 5.1.2 on 2024-11-05 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eezy', '0001_initial'),
        ('tabs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eezy',
            name='tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eezy', to='tabs.tab'),
        ),
    ]
