from django.db import models

class Post(models.Model):
  text = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.text

