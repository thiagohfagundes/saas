# Generated by Django 5.0.8 on 2024-08-28 11:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Customer',
        ),
    ]
