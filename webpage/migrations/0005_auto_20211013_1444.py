# Generated by Django 3.2.7 on 2021-10-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_alter_patientprofile_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientprofile',
            old_name='ocupation',
            new_name='occupation',
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='phone_number',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
