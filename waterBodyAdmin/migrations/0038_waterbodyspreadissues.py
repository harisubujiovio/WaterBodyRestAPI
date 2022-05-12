# Generated by Django 4.0.4 on 2022-05-11 13:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0037_alter_waterbodybasicdetailresponse_surveyresponse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterBodySpreadIssues',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('createdBy', models.CharField(max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedBy', models.CharField(blank=True, max_length=255)),
                ('lastModifiedDate', models.DateTimeField(auto_now=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waterBodyAdmin.waterbodystreamissues')),
                ('spreadResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Issues', to='waterBodyAdmin.waterbodyspreadresponse')),
            ],
        ),
    ]