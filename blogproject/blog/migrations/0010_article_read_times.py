# Generated by Django 2.0 on 2018-11-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181112_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read_times',
            field=models.PositiveIntegerField(default=0, verbose_name='阅读次数'),
        ),
    ]