# Generated by Django 4.2.6 on 2024-02-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=100)),
                ('text_field', models.TextField()),
                ('file_field', models.FileField(upload_to='files/')),
                ('image_field', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
