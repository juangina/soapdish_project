from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    video = EmbedVideoField()  # same like models.URLField()
    def __str__(self):
        return self.name