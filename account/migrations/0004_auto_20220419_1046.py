# Generated by Django 3.2.13 on 2022-04-19 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_useraccount_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup_otp',
            name='user',
        ),
        migrations.RemoveField(
            model_name='address',
            name='Name',
        ),
        migrations.DeleteModel(
            name='forget_otp',
        ),
        migrations.DeleteModel(
            name='signup_otp',
        ),
    ]
