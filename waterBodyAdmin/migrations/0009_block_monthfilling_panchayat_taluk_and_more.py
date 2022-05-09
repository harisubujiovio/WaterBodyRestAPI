# Generated by Django 4.0.3 on 2022-05-07 01:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0008_tankmetadata_tankid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
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
            name='MonthFilling',
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
            name='Panchayat',
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
            name='Taluk',
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
            name='WaterBodyOwnerShip',
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
            name='WaterBodyType',
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
