from django.db import models

# Create your models here.


class UserFile(models.Model):
    # Store the path of the file in the db and the file will be on the hard drive
    # File will be stored in the folder "files" in the DIR selected in settings.py
    file = models.FileField(upload_to="files")
