# Generated by Django 3.2 on 2021-12-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_auto_20211211_1729'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TermUser',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='agree',
            field=models.BooleanField(default=True),
        ),
    ]
