# Generated by Django 4.0.4 on 2022-07-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0006_remove_waterbodysurveyresponse_uniqueid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterbodysurveyresponse',
            name='uniqueid',
            field=models.CharField(default='', max_length=255),
        ),
    ]
