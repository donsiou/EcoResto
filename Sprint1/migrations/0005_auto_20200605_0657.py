# Generated by Django 3.0.5 on 2020-06-05 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sprint1', '0004_auto_20200605_0628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='_tel',
            new_name='tel',
        ),
    ]
