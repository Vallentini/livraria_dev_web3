# Generated by Django 5.2 on 2025-04-15 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_livro_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='coautor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='livros_coautor', to='core.autor'),
        ),
    ]
