# Generated by Django 3.0 on 2019-12-09 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='curators',
            field=models.ManyToManyField(related_name='curators', to=settings.AUTH_USER_MODEL, verbose_name='Кураторы'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teacher', to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
    ]
