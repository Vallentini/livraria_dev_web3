# Generated by Django 5.2.1 on 2025-05-27 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_livro_capa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='capa',
        ),
    ]
