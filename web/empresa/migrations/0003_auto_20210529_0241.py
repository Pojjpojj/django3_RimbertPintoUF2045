# Generated by Django 3.2 on 2021-05-29 00:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_alter_empresa_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Título'),
        ),
    ]
