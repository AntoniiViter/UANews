# Generated by Django 4.0.4 on 2022-05-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_comments_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='info',
            field=models.TextField(verbose_name='текст комментария'),
        ),
    ]
