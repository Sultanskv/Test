# Generated by Django 3.2.24 on 2024-08-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_admin', '0019_alter_sub_admindt_subadmin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_admindt',
            name='subadmin_id',
            field=models.CharField(default='f0fa2f07', max_length=8, unique=True),
        ),
    ]
