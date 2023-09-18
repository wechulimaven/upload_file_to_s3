from django.db import models

# Create your models here.

class Files(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    name = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return self.name