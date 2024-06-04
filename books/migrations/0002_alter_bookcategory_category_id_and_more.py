# Generated by Django 4.1 on 2024-05-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcategory',
            name='category_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bookcode',
            name='code_id',
            field=models.CharField(max_length=1, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
