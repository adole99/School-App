# Generated by Django 3.2.8 on 2023-01-04 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20230104_2036'),
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentClass',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
