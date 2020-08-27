# Generated by Django 3.0.8 on 2020-07-22 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0039_ordershipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordershipping',
            name='id',
        ),
        migrations.AddField(
            model_name='ordershipping',
            name='Cart',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main_app.Cart'),
            preserve_default=False,
        ),
    ]