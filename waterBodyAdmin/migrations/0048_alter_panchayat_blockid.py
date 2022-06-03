# Generated by Django 4.0.4 on 2022-05-28 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waterBodyAdmin', '0047_remove_waterbodyspreadresponse_issues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panchayat',
            name='blockId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panchayats', to='waterBodyAdmin.block'),
        ),
    ]
