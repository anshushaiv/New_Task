from distutils.command.upload import upload
from django.db import models

# Create your models here.

class MP_files(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    data_file = models.FileField(upload_to="files")
    file_name = models.CharField(max_length=100, null=True, blank=True)
    upload_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Uploaded_Data"