# Generated by Django 4.2.5 on 2023-10-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appExpe', '0006_evento_texto_notas_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='url',
            field=models.URLField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='notas',
            name='url',
            field=models.URLField(max_length=250, null=True),
        ),
    ]
