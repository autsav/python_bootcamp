# Generated by Django 3.2.5 on 2021-08-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelpractice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='bio',
            field=models.CharField(max_length=200, null=True),
        ),
    ]