# Generated by Django 4.2.5 on 2023-09-15 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0003_movie_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.AUTH_USER_MODEL, verbose_name='Владелец фильма'),
        ),
    ]
