# Generated by Django 3.1.5 on 2021-07-11 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AidLink', '0007_auto_20210711_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='volunteer_id',
            new_name='volunteers_id',
        ),
    ]
