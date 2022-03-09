from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posterr.models import User

@api_view(['GET'])
def follow(request, user, friend):
  try:
    user = User.objects.get(pk=user)
    friend = User.objects.get(pk=friend)
    user.friends.add(friend)
    user.save()
    return Response({"message":"ok"})
  except User.DoesNotExist:
    raise Http404


@api_view(['GET'])
def unfollow(request, user, friend):
  try:
    user = User.objects.get(pk=user)
    friend = User.objects.get(pk=friend)
    user.friends.remove(friend)
    user.save()
    return Response({"message":"ok"})
  except User.DoesNotExist:
    raise Http404
