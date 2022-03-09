from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from posterr.models import User
from posterr.serializers import UserSerializer

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
      serializer = UserSerializer(data=request.data)
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