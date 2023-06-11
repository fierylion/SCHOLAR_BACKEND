from django.db import models

# Create your models here.
class Lecturers(models.Model):
    name = models.CharField(max_length=40, blank=False)
    link = models.CharField(max_length=300, blank=False)
    def __str__(self):
        return f'Lecurer {self.name}'
    
 