# Generated by Django 4.0.4 on 2022-07-24 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0009_waterbodysource1response_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waterbodyfreecatchmentresponse',
            name='sourcecontributiontype',
        ),
    ]
