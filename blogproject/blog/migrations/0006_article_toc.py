# Generated by Django 2.0 on 2018-11-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181108_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='toc',
            field=models.CharField(default='nihao', editable=False, max_length=400, verbose_name='导航'),
            preserve_default=False,
        ),
    ]