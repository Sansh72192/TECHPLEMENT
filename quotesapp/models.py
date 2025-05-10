from django.db import models

class Quote(models.Model):
    text = models.TextField(unique=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'"{self.text}" — {self.author}'