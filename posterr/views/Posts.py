from rest_framework.response import Response
from rest_framework.views import APIView

from posterr.models import User, Post
from posterr.serializers import PostSerializer


class PostCreate(APIView):
  '''
    Create Posts
  '''

  def post(self, request):
    try:

      user = User.objects.get(pk=request.data['poster'])
      
      serializer_data = {
        'content':request.data['content'],
        'poster': user.username
      }
      
      serializer = PostSerializer(data=serializer_data)
      
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
      message = {
        "exception": str(e.__class__),
        "message": e.args[0]
      }
      return Response(message, status=500)