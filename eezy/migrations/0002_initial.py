# Generated by Django 5.1.2 on 2024-11-15 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eezy', '0001_initial'),
        ('tabs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eezy',
            name='tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eezies', to='tabs.tab'),
        ),
    ]