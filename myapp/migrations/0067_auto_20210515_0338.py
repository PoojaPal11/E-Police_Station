# Generated by Django 3.2 on 2021-05-14 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0066_auto_20210515_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_inspector',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sub_inspector',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sub_inspector',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
