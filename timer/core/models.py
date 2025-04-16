from django.db import models

# Create your models here.
class Note(models.Model):
    date = models.DateField()
    note = models.TextField(default='')
    priority = models.IntegerField()

    def __str__(self):
        return self.note