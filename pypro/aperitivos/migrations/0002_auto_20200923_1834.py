# Generated by Django 3.1.1 on 2020-09-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitivos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(max_length=30),
        ),
    ]
