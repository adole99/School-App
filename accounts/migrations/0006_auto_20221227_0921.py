# Generated by Django 3.2.8 on 2022-12-27 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentClass',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
