# Generated by Django 2.2.1 on 2019-06-07 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_administrationpublique_mairie_maison'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Eleve',
        ),
        migrations.RemoveField(
            model_name='mairie',
            name='administrationpublique_ptr',
        ),
        migrations.DeleteModel(
            name='Maison',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='lieu_ptr',
        ),
        migrations.DeleteModel(
            name='RestoProxy',
        ),
        migrations.DeleteModel(
            name='AdministrationPublique',
        ),
        migrations.DeleteModel(
            name='Lieu',
        ),
        migrations.DeleteModel(
            name='Mairie',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
