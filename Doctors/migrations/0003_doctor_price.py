# Generated by Django 3.2.23 on 2024-01-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0002_rename_doctors_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]