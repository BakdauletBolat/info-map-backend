# Generated by Django 5.0.6 on 2024-06-23 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeometryObjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.FileField(upload_to='categoryIcons/')),
            ],
        ),
        migrations.CreateModel(
            name='GeometryObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geometry', models.JSONField()),
                ('info', models.JSONField()),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.village')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='geometry.geometryobjectcategory')),
            ],
        ),
    ]
