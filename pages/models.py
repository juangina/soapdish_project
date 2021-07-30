from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    videoURL = EmbedVideoField()  # same like models.URLField()
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-added']