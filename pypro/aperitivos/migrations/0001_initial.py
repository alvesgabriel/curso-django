# Generated by Django 3.1.1 on 2020-09-22 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=30)),
                ('vimeo_id', models.CharField(max_length=30)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
