# Generated by Django 2.0.6 on 2018-10-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_mentor_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='bio',
            field=models.CharField(default='none', max_length=300),
        ),
    ]
