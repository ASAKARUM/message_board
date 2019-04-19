from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    thumbs_up = models.PositiveIntegerField(default=0)
    thumbs_down = models.PositiveIntegerField(default=0)


class Record(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post_id = models.CharField(max_length=100, default="")
    is_like = models.BooleanField(default=False)
    


