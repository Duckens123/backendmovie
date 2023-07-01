from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Acteur, Film, Realisateur, Avis
from .serializers import ActeurSerializer, FilmSerializer, RealisateurSerializer, AvisSerializer

#****************************GET********************************

@api_view(['GET'])
def acteur_list(request):
    acteurs = Acteur.objects.all()
    serializer = ActeurSerializer(acteurs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def acteur_detail(request, pk):
    acteur = Acteur.objects.get(pk=pk)
    serializer = ActeurSerializer(acteur)
    return Response(serializer.data)

@api_view(['GET'])
def film_list(request):
    films = Film.objects.all()
    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def film_detail(request, pk):
    film = Film.objects.get(pk=pk)
    serializer = FilmSerializer(film)
    return Response(serializer.data)

@api_view(['GET'])
def realisateur_list(request):
    realisateurs = Realisateur.objects.all()
    serializer = RealisateurSerializer(realisateurs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def realisateur_detail(request, pk):
    realisateur = Realisateur.objects.get(pk=pk)
    serializer = RealisateurSerializer(realisateur)
    return Response(serializer.data)

@api_view(['GET'])
def avis_list(request):
    avis = Avis.objects.all()
    serializer = AvisSerializer(avis, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def avis_detail(request, pk):
    avis = Avis.objects.get(pk=pk)
    serializer = AvisSerializer(avis)
    return Response(serializer.data)



#*********************************POST***********************************

@api_view(['POST'])
def acteur_create(request):
    serializer = ActeurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def film_create(request):
    serializer = FilmSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def realisateur_create(request):
    serializer = RealisateurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def avis_create(request):
    serializer = AvisSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)