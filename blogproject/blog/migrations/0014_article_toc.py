# Generated by Django 2.0 on 2018-11-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_article_toc'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='toc',
            field=models.TextField(default='ceshi', editable=False, verbose_name='导航'),
            preserve_default=False,
        ),
    ]