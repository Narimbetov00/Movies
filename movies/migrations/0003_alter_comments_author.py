# Generated by Django 4.2 on 2024-07-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.CharField(max_length=150),
        ),
    ]
