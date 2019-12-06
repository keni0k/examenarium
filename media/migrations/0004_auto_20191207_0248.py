# Generated by Django 3.0 on 2019-12-06 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20191207_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='dir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Catalog'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, help_text='Описание фото', max_length=100),
        ),
    ]
