from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 128, unique = True)
    authors = models.CharField(max_length = 255)
    language = models.CharField(max_length = 255)
    technology = models.CharField(max_length = 255)
    screenshot = models.CharField(max_length = 128)
    description = models.TextField()

    def __str__(self):
        return self.title
