# Generated by Django 3.2 on 2021-04-29 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_taluka'),
    ]

    operations = [
        migrations.AddField(
            model_name='taluka',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.city'),
        ),
    ]
