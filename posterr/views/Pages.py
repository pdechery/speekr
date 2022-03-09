from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from posterr.models import User, Post, Repost, Quote
from posterr.serializers import UserSerializer, PostSerializer, RepostSerializer, QuoteSerializer

# HTML

def HomePage(request):
  return render(request, 'home.html')

def Profile(request, user):
  return render(request, 'profile.html')


# API

@api_view(['GET','POST'])
def home(request):

  pk = None
  
  if request.method == 'POST':
    pk = request.data['user']

  try:

    posts = Post.objects.all()
    if pk:
      posts = Post.objects.filter(poster=pk)
    post_serializer = PostSerializer(posts, many=True)

    reposts = Repost.objects.all()
    if pk:
      reposts = Repost.objects.filter(reposter=pk)
    repost_serializer = RepostSerializer(reposts, many=True)

    quotes = Quote.objects.all()
    if pk:
      quotes = Quote.objects.filter(quoter=pk)
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

    following = user.friends.count() # qtos adicionei
    #followers = User.objects.filter(related_to=user).count()
    followers = user.related_to.count() # qtos me adicionaram

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


