# Generated by Django 4.2.7 on 2023-12-05 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Libraryapp', '0004_remove_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Name',
            new_name='book_name',
        ),
        migrations.AddField(
            model_name='book',
            name='business_book',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='coding_books',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='', upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='friction_books',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='recommended_books',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='summery',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='Libraryapp.category'),
        ),
    ]
