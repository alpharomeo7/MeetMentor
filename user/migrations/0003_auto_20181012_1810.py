# Generated by Django 2.0.6 on 2018-10-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default='123456', max_length=511),
        ),
        migrations.AlterField(
            model_name='user',
            name='forgot_code',
            field=models.CharField(default='random', max_length=6),
        ),
    ]