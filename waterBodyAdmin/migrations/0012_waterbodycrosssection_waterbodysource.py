# Generated by Django 4.0.3 on 2022-05-08 02:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0011_rename_monthfilling_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterBodyCrossSection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBodySource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
