# Generated by Django 4.2.5 on 2023-10-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appExpe', '0007_evento_url_notas_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imagen2',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='evento',
            name='imagen3',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='notas',
            name='imagen2',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='notas',
            name='imagen3',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]