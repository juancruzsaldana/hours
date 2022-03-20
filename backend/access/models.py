from django.db import models

class Access(models.Model):
    service = models.CharField(max_length=200)
    url = models.CharField(max_length=1000, blank=True, null=True)
    user = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    observations = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name