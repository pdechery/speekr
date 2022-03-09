from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class User(AbstractUser):
  name = models.CharField(max_length=14, unique=True)
  friends = models.ManyToManyField("self", symmetrical=False, related_name='related_to', blank=True)
  creation_date = models.DateField(auto_now_add=True)

  def save(self, *args, **kwargs):
    if not self.username:
      import random
      self.username = 'poster_'+str(random.randint(10,100))
    super().save(*args, **kwargs)


class Post(models.Model):
  poster = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
  content = models.CharField(max_length=777)
  date = models.DateField(auto_now_add=True)


class Repost(models.Model):
  post = models.ForeignKey(Post, related_name='reposts', on_delete=models.CASCADE)
  reposter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)

  def get_post_content(self):
    post = self.post.content
    return post


class Quote(models.Model):
  post = models.ForeignKey(Post, related_name='quotes', on_delete=models.CASCADE)
  quote = models.CharField(max_length=200)
  quoter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)

