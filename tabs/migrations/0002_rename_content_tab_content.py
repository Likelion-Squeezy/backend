# Generated by Django 5.1.2 on 2024-11-01 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tab',
            old_name='Content',
            new_name='content',
        ),
    ]