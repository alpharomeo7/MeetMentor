# Generated by Django 2.0.6 on 2018-10-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='gender',
            field=models.CharField(default='other', max_length=10),
        ),
    ]