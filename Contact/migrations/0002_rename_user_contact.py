# Generated by Django 4.0.5 on 2022-06-25 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Contact',
        ),
    ]
