# Generated by Django 4.2.5 on 2023-10-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appExpe', '0024_alter_artista_imagen_alter_evento_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='expedicioncultural/media'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='expedicioncultural/media'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='imagen2',
            field=models.ImageField(blank=True, upload_to='expedicioncultural/media'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='imagen3',
            field=models.ImageField(blank=True, upload_to='expedicioncultural/media'),
        ),
    ]
