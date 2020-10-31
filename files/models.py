from django.db import models

class File(models.Model):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='files/store')

    def __str__(self):
        return self.title