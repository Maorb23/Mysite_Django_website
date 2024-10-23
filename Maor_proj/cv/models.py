# Maor_proj.cv/models.py

from django.db import models
from django.utils.text import slugify
import os

class CV(models.Model):
    name = models.CharField(max_length=100, default='Maor Blumberg')
    email = models.EmailField(default='maorblumberg@gmail.com')
    phone = models.CharField(max_length=20, default='(+972) 54-327073')
    cv_file = models.FileField(upload_to='cv_files/')  # This field handles the file upload

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.cv_file:
            original_filename = self.cv_file.name
            base, extension = os.path.splitext(original_filename)
            sanitized_filename = f"{slugify(base)}{extension}"
            self.cv_file.name = sanitized_filename
        super().save(*args, **kwargs)
