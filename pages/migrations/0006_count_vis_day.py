# Generated by Django 3.1.1 on 2021-03-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_count_vis_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='vis_day',
            field=models.IntegerField(default=0),
        ),
    ]
