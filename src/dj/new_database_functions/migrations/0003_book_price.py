# Generated by Django 5.1.3 on 2024-12-24 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_database_functions', '0002_book_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=2.2, max_length=3),
        ),
    ]