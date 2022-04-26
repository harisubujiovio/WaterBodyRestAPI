# Generated by Django 4.0.3 on 2022-03-31 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0007_tankimage_alter_userprofile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tankmetadata',
            name='tankId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='images', to='waterBodyAdmin.tankimage'),
        ),
    ]
