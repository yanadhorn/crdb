# Generated by Django 2.1.2 on 2018-11-29 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20181128_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='person_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persons.person'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='organization_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
