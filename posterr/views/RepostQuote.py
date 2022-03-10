from rest_framework.response import Response
from rest_framework.views import APIView

from posterr.models import User, Post
from posterr.serializers import RepostSerializer, QuoteSerializer


class RepostCreate(APIView):
  '''
    Create Repost
  '''
  def post(self, request):
    try:
      
      '''
      Retrieving username from the id passed in the request
      This is needed because the serializer will not accept an id/integer in the 'reposter' field
      '''
      user = User.objects.get(pk=request.data['reposter'])

      serializer = RepostSerializer(data={'reposter': user.username})

      if serializer.is_valid():
        
        '''
        Passing post id to be processed in the serializer's create method.
        This is needed to save a new instance.
        '''
        serializer.save(post_id=request.data['post'])
        return Response(serializer.data)
      return Response(serializer.errors, status=400)


    except Exception as e:
      message = {
        "exception": str(e.__class__),
        "message": e.args[0]
      }
      return Response(message, status=500)


class QuoteCreate(APIView):
  '''
  Create Quote
  Basically same rules as RepostCreate
  '''
  def post(self, request):
    try:

      user = User.objects.get(pk=request.data['quoter'])

      request_data = {
        'quoter': user.username, 
        'quote': request.data['quote']
      }

      serializer = QuoteSerializer(data=request_data)

      if serializer.is_valid():
        serializer.save(post_id=request.data['post'])
        return Response(serializer.data)
      return Response(serializer.errors, status=400)

    except Exception as e:
      message = {
        "exception": str(e.__class__),
        "message": e.args[0]
      }
      return Response(message, status=500)