# Generated by Django 4.0.4 on 2022-07-07 10:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionType',
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
            name='Resource',
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
            name='ResourcePermissions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resourcepermissiontype', to='waterBodyAdmin.permissiontype')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resourcepermissions', to='waterBodyAdmin.resource')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roleresourcepermissions', to='waterBodyAdmin.role')),
            ],
        ),
    ]
