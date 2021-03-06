# Generated by Django 2.2.1 on 2019-06-07 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190607_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrationPublique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=255)),
                ('taille', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=255)),
                ('proprietaire', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mairie',
            fields=[
                ('administrationpublique_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.AdministrationPublique')),
                ('maire', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.administrationpublique',),
        ),
    ]
