from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class VideoModel(models.Model):
    video = EmbedVideoField()

