from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from posterr.models import User, Post, Repost, Quote
from posterr.serializers import UserSerializer, PostSerializer, RepostSerializer, QuoteSerializer


@api_view(['GET'])
def home(request):

  try:
    posts = Post.objects.all()
    post_serializer = PostSerializer(posts, many=True)

    reposts = Repost.objects.all()
    repost_serializer = RepostSerializer(reposts, many=True)

    quotes = Quote.objects.all()
    quote_serializer = QuoteSerializer(quotes, many=True)

    return Response({
      "posts": post_serializer.data,
      "reposts": repost_serializer.data,
      "quotes": quote_serializer.data
    })
  except:
    raise Http404


@api_view(['GET'])
def profile(request, user):

  user = User.objects.get(pk=user)
  user_serializer = UserSerializer(user)

  posts = Post.objects.filter(poster=user)
  post_serializer = PostSerializer(posts, many=True)

  reposts = Repost.objects.filter(reposter=user)
  repost_serializer = RepostSerializer(reposts, many=True)

  quotes = Quote.objects.filter(quoter=user)
  quote_serializer = QuoteSerializer(quotes, many=True)

  following = user.friends.count()
  followers = User.objects.filter(related_to=user).count()

  return Response({
    "user": user_serializer.data,
    "following": following,
    "followers": followers,
    "posts": post_serializer.data,
    "reposts": repost_serializer.data,
    "quotes": quote_serializer.data
  })


