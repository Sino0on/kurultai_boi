# Generated by Django 4.1.2 on 2023-02-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_remove_news_content_af_remove_news_content_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]