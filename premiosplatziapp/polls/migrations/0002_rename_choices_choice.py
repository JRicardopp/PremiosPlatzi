# Generated by Django 4.1 on 2022-08-16 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='choices',
            new_name='Choice',
        ),
    ]
