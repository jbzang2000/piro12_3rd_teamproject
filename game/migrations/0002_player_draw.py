# Generated by Django 2.2.9 on 2020-01-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='draw',
            field=models.IntegerField(default=0),
        ),
    ]
