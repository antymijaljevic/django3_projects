# Generated by Django 3.0.3 on 2020-03-08 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200308_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='data_created',
            new_name='date_created',
        ),
    ]
