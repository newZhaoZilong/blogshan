# Generated by Django 2.0 on 2018-11-08 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
    ]
