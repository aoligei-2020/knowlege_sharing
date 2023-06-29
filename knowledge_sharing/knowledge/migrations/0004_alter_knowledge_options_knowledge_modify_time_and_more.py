# Generated by Django 4.2.2 on 2023-06-19 04:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0003_alter_knowledge_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='knowledge',
            options={'verbose_name': 'Knowledge', 'verbose_name_plural': 'Knowledge'},
        ),
        migrations.AddField(
            model_name='knowledge',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content'),
        ),
    ]
