# Generated by Django 4.0 on 2021-12-14 15:26
from dbview.helpers import CreateView
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('uid', models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False)),
                ('poan', models.CharField(blank=True, max_length=100, null=True)),
                ('soan', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('locality', models.CharField(blank=True, max_length=100, null=True)),
                ('town', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('county', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CsvData',
            fields=[
                ('uid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('property_type', models.CharField(choices=[('D', 'Detached'), ('S', 'Semi-Detached'), ('T', 'Terraced'), ('F', 'Flat'), ('O', 'Other')], max_length=1)),
                ('new', models.BooleanField()),
                ('duration', models.CharField(choices=[('F', 'Freehold'), ('L', 'Leasehold')], max_length=1)),
                ('poan', models.CharField(blank=True, max_length=100, null=True)),
                ('soan', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('locality', models.CharField(blank=True, max_length=100, null=True)),
                ('town', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('county', models.CharField(blank=True, max_length=100, null=True)),
                ('standard', models.CharField(choices=[('A', 'Standard'), ('B', 'Repo')], max_length=1)),
                ('record', models.CharField(choices=[('A', 'Add'), ('D', 'Delete'), ('C', 'Change')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('uid', models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=2)),
                ('district', models.CharField(max_length=2)),
                ('sector', models.IntegerField()),
                ('unit', models.CharField(max_length=2)),
            ],
        ),
        CreateView(
            name='UniquePostcodes',
            fields=[
                ('postcode', models.CharField(primary_key=True, blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('uid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('property_type', models.CharField(choices=[('D', 'Detached'), ('S', 'Semi-Detached'), ('T', 'Terraced'), ('F', 'Flat'), ('O', 'Other')], max_length=1)),
                ('new', models.BooleanField()),
                ('duration', models.CharField(choices=[('F', 'Freehold'), ('L', 'Leasehold')], max_length=1)),
                ('standard', models.CharField(choices=[('A', 'Standard'), ('B', 'Repo')], max_length=1)),
                ('record', models.CharField(choices=[('A', 'Add'), ('D', 'Delete'), ('C', 'Change')], default='A', max_length=1)),
                ('Address', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='house_prices.address')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='postcode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='house_prices.postcode'),
        ),
    ]
