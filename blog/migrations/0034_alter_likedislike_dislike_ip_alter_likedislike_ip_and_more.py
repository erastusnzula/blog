# Generated by Django 4.0.1 on 2022-04-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_likedislike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedislike',
            name='dislike_ip',
            field=models.BooleanField(blank=True, null=True, verbose_name=False),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='ip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='like_ip',
            field=models.BooleanField(blank=True, null=True, verbose_name=False),
        ),
    ]
