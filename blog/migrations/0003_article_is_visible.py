# Generated by Django 2.2.1 on 2019-05-28 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_visible',
            field=models.BooleanField(default=False, verbose_name='Article publié ?'),
        ),
    ]
