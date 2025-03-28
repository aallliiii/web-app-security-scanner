from django.db import models
import hashlib

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    sha256_hash=models.CharField(max_length=64, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs):
        # Generate SHA-256 hash before saving
        if not self.sha256_hash:
            h = hashlib.sha256()
            for chunk in self.file.chunks():
                h.update(chunk)
            self.sha256_hash=h.hexdigest()
        super().save(*args, **kwargs)
