# Generated by Django 3.2.5 on 2021-08-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelextra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbio',
            name='bio',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
