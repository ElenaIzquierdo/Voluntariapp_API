# Generated by Django 3.0 on 2019-12-11 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariapp', '0012_cours_quarter_setmana'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='setmana',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='voluntariapp.Setmana'),
            preserve_default=False,
        ),
    ]
