from django.db import models
from gdstorage.storage import GoogleDriveStorage


gd_storage = GoogleDriveStorage()

class MyModel(models.Model):
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()
    file_field = models.FileField(upload_to='files/', storage=gd_storage) 
    image_field = models.ImageField(upload_to='images/', storage=gd_storage)  
