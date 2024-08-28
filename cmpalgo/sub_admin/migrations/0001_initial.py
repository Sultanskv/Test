# Generated by Django 5.0.4 on 2024-07-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sub_adminDT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subadmin_id', models.CharField(default='501febdd', max_length=8, unique=True)),
                ('subadmin_name_first', models.CharField(blank=True, max_length=50, null=True)),
                ('subadmin_name_last', models.CharField(blank=True, max_length=50, null=True)),
                ('subadmin_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subadmin_password', models.CharField(blank=True, max_length=50, null=True)),
                ('subadmin_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('subadmin_verify_code', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
