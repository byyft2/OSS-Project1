# Generated by Django 2.1.8 on 2019-06-01 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_continent_blog_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='continent',
            old_name='continent_count',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='continent',
            old_name='continent_name',
            new_name='name',
        ),
    ]
