# Generated by Django 3.2.9 on 2021-11-03 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0010_cornerstonecoursekey'),
    ]

    operations = [
        migrations.AddField(
            model_name='cornerstoneenterprisecustomerconfiguration',
            name='session_token',
            field=models.CharField(blank=True, help_text="The most current session token provided for authorization to make API calls to the customer's instance", max_length=255, verbose_name='Cornerstone Session Token'),
        ),
        migrations.AddField(
            model_name='cornerstoneenterprisecustomerconfiguration',
            name='session_token_modified',
            field=models.DateTimeField(blank=True, help_text='Date time when session token was last provided', null=True),
        ),
        migrations.AddField(
            model_name='historicalcornerstoneenterprisecustomerconfiguration',
            name='session_token',
            field=models.CharField(blank=True, help_text="The most current session token provided for authorization to make API calls to the customer's instance", max_length=255, verbose_name='Cornerstone Session Token'),
        ),
        migrations.AddField(
            model_name='historicalcornerstoneenterprisecustomerconfiguration',
            name='session_token_modified',
            field=models.DateTimeField(blank=True, help_text='Date time when session token was last provided', null=True),
        ),
    ]
