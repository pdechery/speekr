from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from speekr.models import User, Post
from speekr.serializers import PostSerializer


class PostCreate(APIView):
  '''
    Create Posts
  '''

  def isAllowed(self, user_id):

    '''
    User cannot make more than 5 posts a day
    Returns false if this rule is broken, true otherwise
    '''
    today = datetime.today()

    todays_posts = Post.objects.filter(poster=user_id).filter(date__day=today.day)

    if todays_posts.count() >= 5:
      return False

    return True


  def post(self, request):
    
    try:

      user_id = request.data['poster']

      if not self.isAllowed(user_id):
        return Response({"message":"You shouldn't make more than 5 posts a day"}, status=status.HTTP_400_BAD_REQUEST)

      user = User.objects.get(pk=user_id)
      
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