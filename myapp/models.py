from django.db import models

class MyModel(models.Model):
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()
    file_field = models.FileField(upload_to='files/')
    image_field = models.ImageField(upload_to='images/')
