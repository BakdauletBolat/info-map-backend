# Generated by Django 5.0.6 on 2024-06-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='latitude',
            field=models.DecimalField(decimal_places=17, default=1, max_digits=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='longitude',
            field=models.DecimalField(decimal_places=17, default=1, max_digits=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='zoom',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='village',
            name='latitude',
            field=models.DecimalField(decimal_places=17, default=1, max_digits=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='village',
            name='longitude',
            field=models.DecimalField(decimal_places=17, default=1, max_digits=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='village',
            name='zoom',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='villagedistrict',
            name='latitude',
            field=models.DecimalField(decimal_places=17, default=1, max_digits=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='villagedistrict',
            name='longitude',
            field=models.DecimalField(decimal_places=17, default=1, max_digits=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='villagedistrict',
            name='zoom',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
