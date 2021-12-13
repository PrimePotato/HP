# Generated by Django 4.0 on 2021-12-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('uid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('postcode', models.CharField(max_length=10)),
                ('property_type', models.CharField(choices=[('D', 'Detached'), ('S', 'Semi-Detached'), ('T', 'Terraced'), ('F', 'Flat'), ('O', 'Other')], max_length=1)),
                ('new', models.BooleanField()),
                ('duration', models.CharField(choices=[('F', 'Freehold'), ('L', 'Leasehold')], max_length=1)),
                ('poan', models.CharField(max_length=100)),
                ('soan', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('standard', models.BooleanField()),
            ],
        ),
    ]