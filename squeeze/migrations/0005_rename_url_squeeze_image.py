# Generated by Django 5.1.2 on 2024-11-16 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squeeze', '0004_remove_squeeze_image_squeeze_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squeeze',
            old_name='url',
            new_name='image',
        ),
    ]
