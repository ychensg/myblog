# Generated by Django 2.1 on 2018-09-01 12:34

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180901_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Content',
            field=DjangoUeditor.models.UEditorField(verbose_name='内容'),
        ),
    ]