from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Videojuego
from .serializers import VideojuegoSerializer import requests
from django.shortcuts import render
 
 

@api_view(['GET'])
def listar_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    serializer = VideojuegoSerializer(videojuegos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_videojuego(request, id):
    try:
        videojuego = Videojuego.objects.get(pk=id)
    except Videojuego.DoesNotExist:
        return Response({'error': 'Videojuego no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = VideojuegoSerializer(videojuego)
    return Response(serializer.data)


def juegos_gratuitos(request):
    url = "https://www.freetogame.com/api/games"
    params = {
        "platform": "pc"
    }
    response = requests.get(url, params=params)
    juegos = response.json() if response.status_code == 200 else []
    return render(request, 'juegos_gratuitos.html', {'juegos': juegos})
