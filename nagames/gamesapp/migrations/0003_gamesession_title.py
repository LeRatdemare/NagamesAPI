# Generated by Django 4.2.9 on 2024-03-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0002_alter_gamesession_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesession',
            name='title',
            field=models.CharField(default='Un jeu random', max_length=100),
            preserve_default=False,
        ),
    ]
