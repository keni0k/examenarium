# Generated by Django 3.0 on 2019-12-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_auto_20191207_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Название директории'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Catalog', verbose_name='Наддиректория'),
        ),
        migrations.AlterField(
            model_name='image',
            name='dir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Catalog', verbose_name='Директория'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Описание фото'),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(verbose_name='Ссылка на фото'),
        ),
        migrations.AlterField(
            model_name='video',
            name='dir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Catalog', verbose_name='Директория'),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название видео'),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(verbose_name='Ссылка (youtube)'),
        ),
    ]
