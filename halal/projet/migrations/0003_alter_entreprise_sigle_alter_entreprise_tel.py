# Generated by Django 4.0.1 on 2022-01-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0002_village_commune'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='sigle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='tel',
            field=models.CharField(max_length=20, verbose_name='Téléphone'),
        ),
    ]
