# Generated by Django 5.0.6 on 2024-12-13 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geometry', '0003_alter_geometryobjectcategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geometryobjectcategory',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
