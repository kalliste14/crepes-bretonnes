# Generated by Django 2.2.1 on 2019-06-08 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_profil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date'], 'permissions': (('commenter_article', 'Commenter un article'), ('marquer_article', 'Marquer un article comme lu')), 'verbose_name': 'article'},
        ),
    ]
