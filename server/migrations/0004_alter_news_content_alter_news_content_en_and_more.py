# Generated by Django 4.1.2 on 2023-02-21 18:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_account_is_aksakal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_ky',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
