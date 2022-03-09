from rest_framework import serializers
from posterr.models import User, Post, Repost, Quote

class UserSerializer(serializers.ModelSerializer):
  friends = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name', many=True)
  class Meta:
    model = User
    fields = ['name','friends']

class PostSerializer(serializers.ModelSerializer):
  poster = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
  
  class Meta:
    model = Post
    fields = ['content','poster','date']

class RepostSerializer(serializers.ModelSerializer): 
  reposter = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
  author = serializers.CharField(source='get_post_author', read_only=True)
  post = serializers.SlugRelatedField(slug_field='content', read_only=True)
  class Meta:
    model = Repost
    fields = ['reposter', 'author', 'date', 'post']

class QuoteSerializer(serializers.ModelSerializer):
  quoter = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
  author = serializers.CharField(source='get_post_author', read_only=True)
  post = serializers.SlugRelatedField(slug_field='content', read_only=True)
  class Meta:
    model = Quote
    fields = ['quoter', 'quote', 'post', 'author', 'date']