# Generated by Django 3.0.8 on 2020-08-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0046_auto_20200828_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordershipping',
            name='address',
            field=models.CharField(help_text='\n    Street address, P.O. box, c/o.\n  ', max_length=30, verbose_name='Address'),
        ),
    ]