# Generated by Django 2.2.6 on 2019-11-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_auto_20191114_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]
