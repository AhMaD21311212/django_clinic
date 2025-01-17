# Generated by Django 3.2.23 on 2024-01-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('mobile', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]
