from django.shortcuts import render
from gamesapp.models import GameSession
from gamesapp.serializers import GameSessionSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def game_sessions(request: HttpRequest):
    if request.method == 'GET':
        data = GameSessionSerializer(GameSession.objects.all(), many=True).data
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        game_session_data = JSONParser().parse(request)
        game_session_serializer = GameSessionSerializer(data=game_session_data)
        if game_session_serializer.is_valid():
            game_session_serializer.save()
            return JsonResponse(game_session_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(game_session_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = GameSession.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)