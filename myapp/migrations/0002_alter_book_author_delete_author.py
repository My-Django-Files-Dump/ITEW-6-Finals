# Generated by Django 5.0.7 on 2025-04-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
