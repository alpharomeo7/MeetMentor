# Generated by Django 2.0.6 on 2018-10-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0004_mentee_connected_mentors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=322)),
                ('code', models.CharField(max_length=32)),
            ],
        ),
    ]