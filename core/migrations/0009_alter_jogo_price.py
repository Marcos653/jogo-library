# Generated by Django 4.0.3 on 2022-04-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_jogo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True),
        ),
    ]
