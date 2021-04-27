from django.db import models
from datetime import datetime

class Plans(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    time_todo = models.DateTimeField(default=datetime.now(), blank=True)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name + "\n" + self.detail
        
