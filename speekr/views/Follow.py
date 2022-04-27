from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from speekr.models import User

@api_view(['GET'])
def isFollowing(request, user1, user2):

  '''
    Checks if auth user follows profile user
    get() method raises excpetion 404 when object doesn't exist
  '''
  
  try:

    if(user1 == user2):
      return Response({"message":"User can't follow himself"}, status=status.HTTP_400_BAD_REQUEST)

    auth_user = User.objects.get(pk=user1)
    relation = auth_user.follows.filter(pk=user2)

    if not relation:
      return Response({"message":"Auth user doesnt follow profile user", "status": 0}, status=status.HTTP_200_OK)
        
    return Response({"message":"Auth user follows profile user", "status": 1}, status=status.HTTP_200_OK)
  
  except User.DoesNotExist:
    raise Http404


@api_view(['POST'])
def doFollow(request):

  '''
    Create a relationship between the autehnticate user and the profile user
    If a specific field exists the relationship will be deleted
  '''

  user1 = request.data['user1']
  user2 = request.data['user2']
  
  try:

    if(user1 == user2):
      return Response({"message":"User can't follow himself"}, status=status.HTTP_400_BAD_REQUEST)
    
    auth_user = User.objects.get(pk=user1)
    
    if not request.data['status']:
      auth_user.follows.remove(user2)
    else:
      auth_user.follows.add(user2)
    
    #auth_user.save()
    
    return Response({"message":"ok"}, status=status.HTTP_200_OK)
  
  except User.DoesNotExist:
    raise Http404

