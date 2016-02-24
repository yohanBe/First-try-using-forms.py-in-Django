from __future__ import unicode_literals

from django.db import models

class blogposts(models.Model):
    name = models.CharField(max_length=15)
    post = models.TextField(max_length=512)
    def __unicode__(self):
        return self.name
