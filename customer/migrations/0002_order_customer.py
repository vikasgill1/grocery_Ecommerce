# Generated by Django 3.2.13 on 2022-04-20 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20220419_1251'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.useraddress'),
        ),
    ]
