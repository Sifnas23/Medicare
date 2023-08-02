# Generated by Django 3.2.10 on 2023-08-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Department', models.CharField(blank=True, max_length=20, null=True)),
                ('Doctor', models.CharField(blank=True, max_length=20, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Time', models.TimeField(blank=True, null=True)),
                ('PhoneNumber', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Place', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]