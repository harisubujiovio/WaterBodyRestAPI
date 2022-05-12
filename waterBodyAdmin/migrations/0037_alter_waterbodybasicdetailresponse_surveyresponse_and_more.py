# Generated by Django 4.0.4 on 2022-05-11 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0036_waterbodybundresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterbodybasicdetailresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BasicDetail', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
        migrations.AlterField(
            model_name='waterbodybundresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bund', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
        migrations.AlterField(
            model_name='waterbodyfreecatchmentresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FreeCatchment', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
        migrations.AlterField(
            model_name='waterbodyhydrologicresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HydrologicParameter', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
        migrations.AlterField(
            model_name='waterbodyirrigationcanalresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IrigationCanal', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
        migrations.AlterField(
            model_name='waterbodysluiceupstreamresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SluiceUpStream', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
        migrations.AlterField(
            model_name='waterbodysourceresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SourceParameter', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
        migrations.AlterField(
            model_name='waterbodyspreadresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Spread', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
        migrations.AlterField(
            model_name='waterbodysurplusfromupstreamresponse',
            name='surveyResponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SurplusFromUpStream', to='waterBodyAdmin.waterbodysurveyresponse'),
        ),
    ]