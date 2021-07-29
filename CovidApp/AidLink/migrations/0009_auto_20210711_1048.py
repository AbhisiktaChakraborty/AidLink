# Generated by Django 3.1.5 on 2021-07-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AidLink', '0008_auto_20210711_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='donordetails',
            name='pincode',
            field=models.CharField(default='700035', max_length=10),
        ),
        migrations.AddField(
            model_name='reciverdetails',
            name='pincode',
            field=models.CharField(default='700035', max_length=10),
        ),
        migrations.AlterField(
            model_name='donations',
            name='amount_raised',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resource',
            name='res_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
