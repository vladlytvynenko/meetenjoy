# Generated by Django 2.2.6 on 2019-12-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0007_meeting_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='photo',
        ),
        migrations.AddField(
            model_name='meeting',
            name='main_photo',
            field=models.FileField(blank=True, null=True, upload_to='meetings/'),
        ),
    ]
