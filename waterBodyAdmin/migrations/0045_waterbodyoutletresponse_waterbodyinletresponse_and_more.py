# Generated by Django 4.0.4 on 2022-05-12 08:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0044_waterbodysurveyresponse_legalissue_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterBodyOutletResponse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('outletnumber', models.IntegerField()),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('outletcondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OutletCondition', to='waterBodyAdmin.waterbodysluicecondition')),
                ('outlettype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InletType', to='waterBodyAdmin.waterbodyoutlettype')),
                ('surveyResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Outlets', to='waterBodyAdmin.waterbodysurveyresponse')),
            ],
        ),
        migrations.CreateModel(
            name='WaterBodyInletResponse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('inletnumber', models.IntegerField()),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('inletcondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InletCondition', to='waterBodyAdmin.waterbodysluicecondition')),
                ('inlettype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InletType', to='waterBodyAdmin.waterbodyinlettype')),
                ('slittrap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SlitTrap', to='waterBodyAdmin.waterbodyslittrap')),
                ('surveyResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Inlets', to='waterBodyAdmin.waterbodysurveyresponse')),
            ],
        ),
        migrations.CreateModel(
            name='WaterBodyGhatsResponse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ghatnumber', models.IntegerField()),
                ('numberofghatsneeded', models.IntegerField()),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('ghatcondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GhatCondition', to='waterBodyAdmin.waterbodyghatcondition')),
                ('surveyResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ghats', to='waterBodyAdmin.waterbodysurveyresponse')),
            ],
        ),
        migrations.CreateModel(
            name='WaterBodyFencingResponse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('fencecondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FenceCondition', to='waterBodyAdmin.waterbodyfencecondition')),
                ('fencetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FenceType', to='waterBodyAdmin.waterbodyfencetype')),
                ('surveyResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fencings', to='waterBodyAdmin.waterbodysurveyresponse')),
            ],
        ),
    ]
