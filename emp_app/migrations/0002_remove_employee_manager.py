# Generated by Django 2.1.5 on 2019-01-11 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='manager',
        ),
    ]
