# Generated by Django 4.1.5 on 2023-01-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_appointment_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='reject',
            field=models.BooleanField(default=False),
        ),
    ]
