# Generated by Django 4.0.4 on 2022-06-26 04:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='block',
            field=models.TextField(blank=b'I01\n'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='district',
            field=models.TextField(blank=b'I01\n'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='division',
            field=models.TextField(blank=b'I01\n'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pincode',
            field=models.IntegerField(blank=b'I00\n', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='region',
            field=models.TextField(blank=b'I01\n'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.TextField(blank=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobileNumber',
            field=models.CharField(max_length=20, unique=b'I01\n'),
        ),
    ]
