from django.db import models
import os

# Create your models here.
#Pag may inupdate ka sa models need mag makemigrations
#then migrate

class File(models.Model):
    file = models.FileField(unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)

    def fileName(self):
        return os.path.basename(self.file.name)