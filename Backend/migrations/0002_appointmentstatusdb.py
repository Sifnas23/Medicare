# Generated by Django 3.2.10 on 2023-08-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointmentstatusdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Time', models.TimeField(blank=True, null=True)),
                ('Status', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
