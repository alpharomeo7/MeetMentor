# Generated by Django 2.0.6 on 2018-10-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0003_mentee_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='connected_mentors',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]