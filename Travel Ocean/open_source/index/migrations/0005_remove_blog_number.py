# Generated by Django 2.1.8 on 2019-05-27 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_blog_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='number',
        ),
    ]
