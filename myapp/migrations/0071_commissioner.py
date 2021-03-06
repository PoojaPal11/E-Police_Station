# Generated by Django 3.2 on 2021-05-14 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0070_alter_constable_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commissioner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='profile_pic')),
                ('Age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('mobile_no', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.commissioner_login')),
            ],
        ),
    ]
