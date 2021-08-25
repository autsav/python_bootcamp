# Generated by Django 3.2.5 on 2021-08-25 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classbased', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('bio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ClassbasedModel',
        ),
    ]
