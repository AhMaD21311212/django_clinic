# Generated by Django 3.2.23 on 2024-02-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0003_doctor_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
