# Generated by Django 3.1.1 on 2021-02-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_count_vis_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='vis_day',
            field=models.IntegerField(default=0),
        ),
    ]