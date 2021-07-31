# Generated by Django 3.2.5 on 2021-07-28 09:48

from django.db import migrations, models
import pandatube.models


class Migration(migrations.Migration):

    dependencies = [
        ('pandatube', '0003_alter_purchasedcourse_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetag',
            name='course_thumbnail',
            field=models.FileField(default='static/default/default-course.jpg', upload_to=pandatube.models.course_thumbnail_path),
        ),
        migrations.AlterField(
            model_name='coursetag',
            name='course_num',
            field=models.IntegerField(unique=True),
        ),
    ]