# Generated by Django 3.2.6 on 2021-08-17 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210809_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
    ]
