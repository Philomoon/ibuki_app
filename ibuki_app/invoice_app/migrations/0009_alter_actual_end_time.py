# Generated by Django 4.2.1 on 2023-10-02 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0008_actual_trans_counts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actual',
            name='end_time',
            field=models.TimeField(default=datetime.time(15, 45), verbose_name='終了時刻'),
        ),
    ]