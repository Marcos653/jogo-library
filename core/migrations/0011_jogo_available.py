# Generated by Django 4.0.3 on 2022-04-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_jogo_storage_jogo_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
