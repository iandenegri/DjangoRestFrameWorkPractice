from django.db import models
from django.conf import settings
import datetime

# Create your models here.

def upload_status_image(instance, filename):
    return 'status/{user}/{filename}'.format(user=instance.user, filename=filename)

class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)

class Status(models.Model): #fb status, tweet
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True, max_length=160)
    image = models.ImageField(upload_to=upload_status_image, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, default=datetime.datetime.now)
    updated = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def __str__(self):
        return str(self.content[:50])

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
