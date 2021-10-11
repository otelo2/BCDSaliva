# Generated by Django 3.2.7 on 2021-10-11 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname_1', models.CharField(max_length=50)),
                ('surname_2', models.CharField(blank=True, max_length=50)),
                ('date_of_birth', models.DateField(max_length=11)),
                ('gender', models.CharField(max_length=7)),
                ('level_of_education', models.CharField(max_length=9)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('ocupation', models.CharField(max_length=50)),
                ('monthly_income', models.CharField(max_length=21)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
