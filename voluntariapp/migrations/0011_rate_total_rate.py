# Generated by Django 3.0 on 2020-01-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariapp', '0010_auto_20200106_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='total_rate',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
