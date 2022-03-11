from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from posterr.models import User, Post, Repost, Quote
from posterr.serializers import UserSerializer, PostSerializer, RepostSerializer, QuoteSerializer

# HTML templates

def HomePage(request):
  return render(request, 'home.html')

def Profile(request, user):
  return render(request, 'profile.html')


# API

@api_view(['GET','POST'])
def home(request):
  '''
  Homepage data with filtering by user
  '''

  try:

    pk = follow_list = None
    
    if request.method == 'POST':
      pk = request.data['user']
      user = User.objects.get(pk=pk)
      follow_list = [user.id for user in user.follows.all()]

    posts = Post.objects.all()
    if follow_list:
      posts = Post.objects.filter(poster__in=follow_list)
    post_serializer = PostSerializer(posts, many=True)

    reposts = Repost.objects.all()
    if follow_list:
      reposts = Repost.objects.filter(reposter__in=follow_list)
    repost_serializer = RepostSerializer(reposts, many=True)

    quotes = Quote.objects.all()
    if follow_list:
      quotes = Quote.objects.filter(quoter__in=follow_list)
    quote_serializer = QuoteSerializer(quotes, many=True)

    return Response({
      "posts": post_serializer.data,
      "reposts": repost_serializer.data,
      "quotes": quote_serializer.data
    })
  
  except Exception as e:
    message = {
      "exception": str(e.__class__),
      "message": e.args[0]
    }
    return Response(message,status=500)


@api_view(['GET'])
def profile(request, user):

  try:

    user = User.objects.get(pk=user)
    user_serializer = UserSerializer(user)

    posts = Post.objects.filter(poster=user)
    post_serializer = PostSerializer(posts, many=True)

    reposts = Repost.objects.filter(reposter=user)
    repost_serializer = RepostSerializer(reposts, many=True)

    quotes = Quote.objects.filter(quoter=user)
    quote_serializer = QuoteSerializer(quotes, many=True)

    following = user.follows.count() 
    #followers = User.objects.filter(following=me)
    followers = user.following.count() 

    return Response({
      "user": user_serializer.data,
      "following": following,
      "followers": followers,
      "posts": post_serializer.data,
      "reposts": repost_serializer.data,
      "quotes": quote_serializer.data
    })

  except Exception as e:
    message = {
      "exception": str(e.__class__),
      "message": e.args[0]
    }
    return Response(message,status=500)


