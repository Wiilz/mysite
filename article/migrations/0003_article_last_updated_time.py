# Generated by Django 2.0.5 on 2018-05-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
