# Generated by Django 4.2.5 on 2023-10-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appExpe', '0002_usuario_rename_genero_artista_generoartista_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='fechaEvento',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='lugarEvento',
            new_name='lugar',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='nombreEvento',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='emailUsuario',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombreUsuario',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='generoArtista',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='nombreArtista',
        ),
        migrations.AddField(
            model_name='artista',
            name='apellido',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='artista',
            name='disciplina',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='artista',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='artista',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
