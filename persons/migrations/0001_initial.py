# Generated by Django 2.1.2 on 2018-11-01 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('edu_id', models.AutoField(primary_key=True, serialize=False)),
                ('edu_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='education_grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_grade', models.CharField(choices=[('x', 'x1'), ('y', 'y1'), ('z', 'z1')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255)),
                ('org_address', models.CharField(max_length=255)),
                ('org_tel', models.CharField(max_length=255)),
                ('org_field', models.CharField(max_length=255)),
                ('org_mail', models.EmailField(max_length=255)),
                ('org_fund', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('summmary', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('email', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('latCo', models.CharField(max_length=255)),
                ('longCo', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('relation', models.CharField(max_length=255)),
                ('Srelation', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('remark', models.TextField()),
                ('edu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.education')),
                ('organization_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.organization')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='edu_grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.education_grade'),
        ),
    ]
