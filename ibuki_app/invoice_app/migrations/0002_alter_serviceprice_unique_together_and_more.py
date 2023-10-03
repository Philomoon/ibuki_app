# Generated by Django 4.2.1 on 2023-09-29 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='serviceprice',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='servicename',
            field=models.CharField(choices=[('A', '日中一時支援（〜４）'), ('B', '日中一時支援（４〜８）'), ('C', '日中一時支援（８〜）'), ('D', '日中一時(併給）'), ('E', '生活介護')], max_length=100),
        ),
        migrations.AddConstraint(
            model_name='serviceprice',
            constraint=models.UniqueConstraint(fields=('insurer', 'service', 'class_obst', 'class_num'), name='unique_fields_combination'),
        ),
    ]