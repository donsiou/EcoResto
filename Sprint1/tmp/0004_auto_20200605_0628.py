# Generated by Django 3.0.5 on 2020-06-05 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Sprint1', '0003_remove_ingredient__quantiteingred'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='_dateNaissance',
            new_name='dateNaissance',
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='_nationalite',
            new_name='nationalite',
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='_nom',
            new_name='profession',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='_dateInscription',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='_email',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='_login',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='_password',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='_prenom',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='_profession',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
