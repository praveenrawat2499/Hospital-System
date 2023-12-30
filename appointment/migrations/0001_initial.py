# Generated by Django 4.1.6 on 2023-12-29 18:28

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
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]