# Generated by Django 4.2.7 on 2023-12-03 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='branch',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='year_Sem',
            new_name='year_sem',
        ),
    ]