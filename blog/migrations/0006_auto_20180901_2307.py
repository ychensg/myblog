# Generated by Django 2.1.1 on 2018-09-01 15:07

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180901_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now, verbose_name='文章标题'),
            preserve_default=False,
        ),
    ]
