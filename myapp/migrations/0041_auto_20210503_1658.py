# Generated by Django 3.2 on 2021-05-03 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_auto_20210503_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fir',
            name='city',
        ),
        migrations.RemoveField(
            model_name='fir',
            name='taluka',
        ),
        migrations.RemoveField(
            model_name='fir',
            name='village',
        ),
    ]
