# Generated by Django 4.0.1 on 2022-03-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_downloadfiles_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='downloadfiles',
            options={'ordering': ['-upload_date'], 'verbose_name_plural': 'Download Files'},
        ),
        migrations.AddField(
            model_name='downloadfiles',
            name='upload_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
