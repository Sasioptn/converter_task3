from django.db import models


class Video(models.Model):
    link = models.CharField(max_length=264)
    email = models.EmailField()

    def __str__(self):
        return self.link
