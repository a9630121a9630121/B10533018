from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=15)
    text = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.title

