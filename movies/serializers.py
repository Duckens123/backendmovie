from rest_framework import serializers
from .models import Acteur, Film, Realisateur, Avis

class ActeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acteur
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    acteurs = serializers.StringRelatedField(many=True)
    realisateur = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Film
        fields = '__all__'

class RealisateurSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True)
    class Meta:
        model = Realisateur
        fields = '__all__'

class AvisSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField()
    film = serializers.StringRelatedField()
    
    class Meta:
        model = Avis
        fields = '__all__'
