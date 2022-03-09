from rest_framework.response import Response
from rest_framework.views import APIView

from posterr.models import Post
from posterr.serializers import PostSerializer

class PostListCreate(APIView):
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