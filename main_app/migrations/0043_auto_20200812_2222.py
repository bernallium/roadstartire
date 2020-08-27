# Generated by Django 3.0.8 on 2020-08-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0042_auto_20200731_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.IntegerField(choices=[(1, 'Current'), (-1, 'Abandoned'), (2, 'In Progress'), (-2, 'Cancelled'), (3, 'Fulfilled')], help_text='\n    <br/>\n    A Cart can be in 1 of 5 states:<br/>\n    🛒 <strong>Current</strong> - The currently open cart (each user can only have 1 cart in this state)<br/>\n    ⏳ <strong>In progress</strong> - Cart has been submitted but not yet fulfilled or cancelled<br/>\n    ✅ <strong>Fulfilled</strong> - Items have been delivered to client and payment has been received<br/>\n    ❌ <strong>Cancelled</strong> - Cart can no longer be fulfilled<br/>\n    🚧 <strong>Abandoned</strong> - The last item in the cart was removed (this will occur automatically)<br/>\n  \n  '),
        ),
    ]