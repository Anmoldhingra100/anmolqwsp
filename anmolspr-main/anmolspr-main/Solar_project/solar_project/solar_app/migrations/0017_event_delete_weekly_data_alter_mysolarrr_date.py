# Generated by Django 5.0.7 on 2024-08-02 07:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0016_rename_daily_production_mysolarrr_energy_distribution_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='weekly_data',
        ),
        migrations.AlterField(
            model_name='mysolarrr',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]