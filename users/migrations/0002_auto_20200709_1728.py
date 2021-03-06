# Generated by Django 3.0.6 on 2020-07-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, help_text='\n    Designates whether this user account should be considered active.<br/>\n    <strong>NOTE:</strong> Only active users can log in.\n  '),
        ),
    ]
