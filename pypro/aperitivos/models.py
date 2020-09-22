from django.db import models
from django.urls import reverse


class Video(models.Model):
    slug = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    vimeo_id = models.CharField(max_length=30)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("aperitivos:video", args=(self.slug,))
