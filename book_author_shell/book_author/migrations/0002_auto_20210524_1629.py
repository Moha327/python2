# Generated by Django 2.2.4 on 2021-05-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.IntegerField(null=True),
        ),
    ]
