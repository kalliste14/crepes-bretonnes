# Generated by Django 2.2.1 on 2019-06-04 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190604_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestoProxy',
            fields=[
            ],
            options={
                'ordering': ['nom'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('blog.restaurant',),
        ),
    ]
