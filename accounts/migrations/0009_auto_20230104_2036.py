# Generated by Django 3.2.8 on 2023-01-04 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_profile_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='guardian_name',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='guardian_phone_number',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='student_class',
        ),
    ]
