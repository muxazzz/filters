# Generated by Django 3.0.8 on 2020-07-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_libr', '0004_auto_20200719_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.SmallIntegerField(choices=[(1, 'механика'), (2, 'автомат'), (3, 'робот')], default=1),
        ),
    ]
