# Generated by Django 4.0.5 on 2022-07-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0012_alter_posteo_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='autor',
            field=models.CharField(default='Anonymo', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posteo',
            name='subtitulo',
            field=models.CharField(default='subtitulo', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posteo',
            name='cuerpo',
            field=models.CharField(max_length=200),
        ),
    ]