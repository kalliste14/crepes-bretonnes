# Generated by Django 2.2.1 on 2019-05-29 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190529_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article'),
        ),
    ]
