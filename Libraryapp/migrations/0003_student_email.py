# Generated by Django 4.2.7 on 2023-12-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libraryapp', '0002_rename_branch_student_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]