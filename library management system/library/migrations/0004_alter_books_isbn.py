# Generated by Django 4.1.1 on 2022-09-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_books_isbn_alter_books_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='ISBN',
            field=models.CharField(max_length=300, primary_key=True, serialize=False, unique=True, verbose_name='ISBN'),
        ),
    ]
