# Generated by Django 4.0.1 on 2022-02-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_like_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike_button',
            field=models.CharField(default='', max_length=255),
        ),
    ]