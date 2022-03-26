# Generated by Django 4.0.1 on 2022-03-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_downloadfiles_linux_downloadfiles_windows_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadfiles',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='downloads/mobile/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='downloadfiles',
            name='linux',
            field=models.FileField(blank=True, default='', null=True, upload_to='downloads/linux/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='downloadfiles',
            name='windows',
            field=models.FileField(blank=True, default='', null=True, upload_to='downloads/windows/%Y/%m/%d/'),
        ),
    ]
