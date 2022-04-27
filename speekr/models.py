from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class User(AbstractUser):
  name = models.CharField(max_length=14, unique=True)
  follows = models.ManyToManyField("self", symmetrical=False, related_name='following', blank=True)
  creation_date = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    '''
      Create automatic username when saving User instance 
    '''
    if not self.username:
      import random
      self.username = 'poster_'+str(random.randint(10,100))
    super().save(*args, **kwargs)


class Post(models.Model):
  poster = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
  content = models.CharField(max_length=777)
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-date',)

  def __str__(self):
    return self.content


class Repost(models.Model):
  post = models.ForeignKey(Post, related_name='reposts', on_delete=models.CASCADE)
  reposter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-date',)

  def get_post_author(self):
    poster = self.post.poster
    return poster


class Quote(models.Model):
  post = models.ForeignKey(Post, related_name='quotes', on_delete=models.CASCADE)
  quote = models.CharField(max_length=200)
  quoter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)

  class Meta:
    ordering = ('-date',)

  def get_post_author(self):
    poster = self.post.poster
    return poster

