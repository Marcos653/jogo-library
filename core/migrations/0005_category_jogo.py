# Generated by Django 4.0.3 on 2022-04-03 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_jogo_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='jogo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.jogo'),
        ),
    ]
