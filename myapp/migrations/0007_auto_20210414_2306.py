# Generated by Django 3.1.7 on 2021-04-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_fir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fir',
            name='FIR_Date_and_Time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
