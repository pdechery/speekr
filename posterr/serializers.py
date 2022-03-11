from rest_framework import serializers
from posterr.models import User, Post, Repost, Quote

# User

class UserSerializer(serializers.ModelSerializer):
  follows = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name', many=True)
  
  class Meta:
    model = User
    fields = ['name','follows','username']


# Post

class PostSerializer(serializers.ModelSerializer):
  poster = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
  
  class Meta:
    model = Post
    fields = ['id','content','poster','date']


# Repost

class RepostSerializer(serializers.ModelSerializer): 
  reposter = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
  author = serializers.CharField(source='get_post_author', read_only=True)
  post = serializers.StringRelatedField(read_only=True)
  
  class Meta:
    model = Repost
    fields = ['reposter', 'author', 'date', 'post']

  def create(self, validated_data):
    post = Post.objects.get(pk=validated_data['post_id'])
    return Repost.objects.create(post=post, reposter=validated_data['reposter'])


# Quote

class QuoteSerializer(serializers.ModelSerializer):
  quoter = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
  author = serializers.CharField(source='get_post_author', read_only=True)
  post = serializers.StringRelatedField(read_only=True)
  
  class Meta:
    model = Quote
    fields = ['quoter', 'quote', 'post', 'author', 'date']

  def create(self, validated_data):
    post = Post.objects.get(pk=validated_data['post_id'])
    return Quote.objects.create(post=post, quoter=validated_data['quoter'], quote=validated_data['quote'])