# Generated by Django 3.2.13 on 2022-04-19 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220419_1046'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Address',
            new_name='UserAddress',
        ),
        migrations.RenameField(
            model_name='useraddress',
            old_name='userAccount',
            new_name='user',
        ),
    ]