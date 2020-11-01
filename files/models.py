from django.db import models
from django.core.exceptions import ValidationError


class File(models.Model):

    def validate_file_extension(value):
        import os
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.pdf', '.pptx']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported! Only .pdf and .pptx accepted')

    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='files/store'
                               , validators=[validate_file_extension])

    def __str__(self):
        return self.title
