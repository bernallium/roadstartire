# Generated by Django 3.0.8 on 2020-07-21 14:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200717_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tax',
            field=models.DecimalField(decimal_places=4, default=0.13, help_text='\n    Tax applied to orders (defaults to <strong>0.13</strong>)\n  ', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Tax'),
        ),
    ]