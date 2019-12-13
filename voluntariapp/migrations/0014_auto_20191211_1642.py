# Generated by Django 3.0 on 2019-12-11 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariapp', '0013_event_setmana'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centreinteres',
            name='description',
        ),
        migrations.RemoveField(
            model_name='centreinteres',
            name='objectius',
        ),
        migrations.RemoveField(
            model_name='centreinteres',
            name='state',
        ),
        migrations.AddField(
            model_name='centreinteres',
            name='name',
            field=models.TextField(default='curs 0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forumtheme',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]