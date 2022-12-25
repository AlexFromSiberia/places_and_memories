from django.db import models
from django.contrib.auth.models import User


class Memory (models.Model):
    place = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # Photos will be saved to (for example path): MEDIA_ROOT/photos/2023/01/30
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photos/default.png')

    class Meta:
        verbose_name_plural = 'Memories'
        # “-” -> reverse order
        ordering = ["-date_added"]

    def __str__(self):
        return self.place

