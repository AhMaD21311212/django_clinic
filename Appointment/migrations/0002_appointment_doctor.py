# Generated by Django 3.2.23 on 2024-01-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]