# Generated by Django 3.2 on 2021-05-06 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_constable_sub_inspector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='Salary',
        ),
    ]
