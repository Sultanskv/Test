# Generated by Django 5.0.4 on 2024-08-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_admin', '0015_alter_sub_admindt_subadmin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_admindt',
            name='subadmin_id',
            field=models.CharField(default='4002ae91', max_length=8, unique=True),
        ),
    ]
