# Generated by Django 3.0.8 on 2020-07-22 01:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0036_auto_20200721_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='discount_ratio_applied',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='tax_applied',
        ),
        migrations.AddField(
            model_name='cart',
            name='discount_percent_applied',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text="\n    • Must be a number from 0.00 to 100.00 (up to 2 decimal places)<br/>\n    • Defaults to using the User's discount ratio<br/>\n  ", max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Discount (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='tax_percent_applied',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text="\n    • Must be a number from 0.00 to 100.00 (up to 2 decimal places)<br/>\n    • Defaults to using the User's tax value<br/>\n  ", max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Tax (%)'),
            preserve_default=False,
        ),
    ]
