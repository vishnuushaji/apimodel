# Generated by Django 4.2.6 on 2024-02-20 10:24

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='file_field',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='image_field',
            field=models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='images/'),
        ),
    ]