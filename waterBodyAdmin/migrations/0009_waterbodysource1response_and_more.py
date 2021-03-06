# Generated by Django 4.0.4 on 2022-07-23 16:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0008_remove_waterbodysurveyresponse_legalissue_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterBodySource1Response',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBodySupplySource1Response',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('surveyResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Source1', to='waterBodyAdmin.waterbodysurveyresponse')),
            ],
        ),
        migrations.DeleteModel(
            name='WaterBodySourceResponse',
        ),
        migrations.AddField(
            model_name='waterbodysource1response',
            name='Source1Response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sources1', to='waterBodyAdmin.waterbodysupplysource1response'),
        ),
        migrations.AddField(
            model_name='waterbodysource1response',
            name='source1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterBodyAdmin.waterbodysource'),
        ),
    ]
