# Generated by Django 3.0 on 2019-12-11 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariapp', '0010_auto_20191211_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='id',
        ),
        migrations.AlterField(
            model_name='rate',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='voluntariapp.Event'),
        ),
    ]
