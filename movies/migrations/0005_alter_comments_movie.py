# Generated by Django 4.2 on 2024-07-11 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_comments_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.movies'),
        ),
    ]
