from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from posterr.models import User, Post, Repost, Quote
from posterr.serializers import UserSerializer, PostSerializer, RepostSerializer, QuoteSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Arbitrary user
DEFAULT_USER_PK = 6

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
    # @todo customize error 500 using JSON not HTML
    pass


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

  return Response({
    "user": user_serializer.data,
    "posts": post_serializer.data,
    "reposts": repost_serializer.data,
    "quotes": quote_serializer.data
  })


class PostList(APIView):
  '''
    List and create Posts
  '''
  def get(self, request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
  '''
    List and create Users
  '''
  def get(self, request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request):
    try:
      serializer = PostSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    except AssertionError as e:
      pass


class UserDetail(APIView):

  def get(self, request, pk):
    try:
      user = User.objects.get(pk=pk)
      serializer = UserSerializer(user)
      return Response(serializer.data)
    except User.DoesNotExist:
      raise Http404

