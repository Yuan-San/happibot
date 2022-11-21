from django.db import models

class Members(models.Model):
  name = models.CharField(max_length=255, default="zero")
  level = models.IntegerField(default=0)
  mood = models.CharField(max_length=10, default="neutral")
  reason = models.CharField(max_length=255, default="lorem ipsum dolor sit amet")
