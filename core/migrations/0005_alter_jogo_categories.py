# Generated by Django 4.0.3 on 2022-04-05 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_jogo_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='core.category'),
        ),
    ]
