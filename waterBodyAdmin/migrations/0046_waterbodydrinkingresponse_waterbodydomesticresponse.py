# Generated by Django 4.0.4 on 2022-05-12 09:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0045_waterbodyoutletresponse_waterbodyinletresponse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterBodyDrinkingResponse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('dependentfamiliesnumber', models.IntegerField()),
                ('dugwellnumber', models.IntegerField()),
                ('depthofdugwell', models.IntegerField()),
                ('numberofborewells', models.IntegerField()),
                ('depthofborewell', models.IntegerField()),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('borewellcondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DrinkingBorewellCondition', to='waterBodyAdmin.waterbodysluicecondition')),
                ('dugwellcondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DrinkingDugwellCondition', to='waterBodyAdmin.waterbodysluicecondition')),
                ('surveyResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Drinkings', to='waterBodyAdmin.waterbodysurveyresponse')),
            ],
        ),
        migrations.CreateModel(
            name='WaterBodyDomesticResponse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('dependentfamiliesnumber', models.IntegerField()),
                ('dependentlivestocksnumber', models.IntegerField()),
                ('dugwellnumber', models.IntegerField()),
                ('depthofdugwell', models.IntegerField()),
                ('numberofborewells', models.IntegerField()),
                ('depthofborewell', models.IntegerField()),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('borewellcondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BorewellCondition', to='waterBodyAdmin.waterbodysluicecondition')),
                ('dugwellcondition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DugwellCondition', to='waterBodyAdmin.waterbodysluicecondition')),
                ('surveyResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Domestics', to='waterBodyAdmin.waterbodysurveyresponse')),
            ],
        ),
    ]