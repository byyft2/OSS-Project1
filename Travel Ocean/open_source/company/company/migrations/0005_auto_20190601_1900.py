# Generated by Django 2.1.8 on 2019-06-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20190601_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continent_blog',
            name='continent',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='continent_blog',
            name='hashtag',
            field=models.CharField(max_length=10),
        ),
    ]