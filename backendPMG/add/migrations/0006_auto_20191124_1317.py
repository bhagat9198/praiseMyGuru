# Generated by Django 2.2.7 on 2019-11-24 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0005_auto_20191124_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcollege',
            name='dateTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 24, 13, 17, 37, 378038)),
        ),
        migrations.AlterField(
            model_name='addschool',
            name='dateTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 24, 13, 17, 37, 378435)),
        ),
        migrations.AlterField(
            model_name='addteacher',
            name='dateTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 24, 13, 17, 37, 377554)),
        ),
    ]