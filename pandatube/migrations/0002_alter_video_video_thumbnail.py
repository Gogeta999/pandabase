# Generated by Django 3.2.5 on 2021-08-11 09:45

from django.db import migrations, models
import pandatube.models


class Migration(migrations.Migration):

    dependencies = [
        ('pandatube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_thumbnail',
            field=models.ImageField(default='default/default-video.jpg', upload_to=pandatube.models.video_thumbnails_path),
        ),
    ]