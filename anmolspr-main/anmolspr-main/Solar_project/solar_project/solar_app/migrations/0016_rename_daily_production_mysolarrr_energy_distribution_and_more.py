# Generated by Django 5.0.7 on 2024-08-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0015_weekly_data_mysolarrr_weekly_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysolarrr',
            old_name='daily_production',
            new_name='Energy_Distribution',
        ),
        migrations.RenameField(
            model_name='mysolarrr',
            old_name='hourly_temperature',
            new_name='Irradiance',
        ),
        migrations.RenameField(
            model_name='mysolarrr',
            old_name='invertor_power_distribution',
            new_name='Profit_and_loss',
        ),
        migrations.RenameField(
            model_name='mysolarrr',
            old_name='monthly_sales',
            new_name='Rain_prediction',
        ),
        migrations.RenameField(
            model_name='mysolarrr',
            old_name='total_panels',
            new_name='UV_index',
        ),
        migrations.RenameField(
            model_name='mysolarrr',
            old_name='weekly_revenue',
            new_name='efficiency',
        ),
        migrations.RemoveField(
            model_name='mysolarrr',
            name='weekly_data',
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='faulty_panels',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='invertor_power_conversion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='maintainance_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='production',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='revenue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='temperature',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='working_panels',
            field=models.IntegerField(default=0),
        ),
    ]
